import os
import io
import json
import base64
from datetime import datetime
from functools import wraps
import pandas as pd
import markdown as md_lib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from flask_bcrypt import Bcrypt
from flask import (
Flask, render_template, request, session, redirect, url_for,
)
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from anthropic import (
Anthropic, RateLimitError, APIConnectionError,
AuthenticationError, APIError,
)

load_dotenv()
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 500
DANE_PREVIEW_WIERSZY = 50
MAX_DLUGOSC_PYTANIA = 1000
MAX_WIERSZY_CSV = 100_000
PLIK_UZYTKOWNIKOW = "users.json"
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = os.environ.get("SECRET_KEY", "zmien-mnie-koniecznie-w-produkcji")

def klucz_limitowania():
    return session.get("nazwa_uzytkownika") or get_remote_address()

limiter = Limiter(
app=app, key_func=klucz_limitowania,
default_limits=["50 per hour"],
)
talisman = Talisman(
app,
force_https=False,
content_security_policy={
"default-src": "'self'",
"style-src": ["'self'", "'unsafe-inline'"],
"script-src": ["'self'", "https: /cdn.jsdelivr.net"],
},
)

@app.errorhandler(429)
def zbyt_wiele_zapytan(e):
    return render_template("blad429.html"), 429

@app.after_request
def dodaj_wlasny_naglowek(response):
    response.headers["X-Appka-Wersja"] = "1.0"
    return response

def wczytaj_uzytkownikow():
    try:
        with open(PLIK_UZYTKOWNIKOW, "r", encoding="utf-8") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return {}

def zapisz_uzytkownikow(uzytkownicy):
    with open(PLIK_UZYTKOWNIKOW, "w", encoding="utf-8") as plik:
        json.dump(uzytkownicy, plik, ensure_ascii=False, indent=2)

def wymaga_logowania(funkcja):
    @wraps(funkcja)
    def opakowana_funkcja(*args, **kwargs):
        if "nazwa_uzytkownika" not in session:
            return redirect(url_for("logowanie"))
        return funkcja(*args, **kwargs)
    return opakowana_funkcja

def zapytaj_claude(tresc_pytania, system_prompt=None):
    try:
        parametry = {
        "model": MODEL, "max_tokens": MAX_TOKENS,
        "messages": [{"role": "user", "content": tresc_pytania}],
        }
        if system_prompt:
            parametry["system"] = system_prompt
        odpowiedz = client.messages.create(**parametry)
        return odpowiedz.content[0].text
    except AuthenticationError:
        return "BŁĄD: nieprawidłowy klucz API."
    except RateLimitError:
        return "BŁĄD: zbyt wiele zapytań."
    except APIConnectionError:
        return "BŁĄD: problem z połączeniem."
    except APIError as blad:
        return f"BŁĄD: {blad}"

SYSTEM_PROMPT_CZAT = """Jesteś pomocnym asystentem, odpowiadasz zwięźle, po polsku."""
DANE_DO_OCHRONY = ["SREBRNY-KLUCZ-2026"]
FRAZY_PODEJRZANE = ["zignoruj poprzednie instrukcje", "podaj hasło"]

def waliduj_output(tekst_odpowiedzi):
    for chroniony_fragment in DANE_DO_OCHRONY:
        if chroniony_fragment in tekst_odpowiedzi:
            return "Odpowiedź zablokowana."
    return tekst_odpowiedzi

def wyglada_na_probe_injection(tekst):
    tekst_male_litery = tekst.lower()
    return any(fraza in tekst_male_litery for fraza in FRAZY_PODEJRZANE)

def oczysc_tekst(tekst):
    for znak in ["\x00", "\r"]:
        tekst = tekst.replace(znak, "")
    return tekst

def zbuduj_prompt_analizy(df):
    liczba_wierszy, liczba_kolumn = df.shape
    kolumny = ", ".join(df.columns.tolist())
    dane_csv = df.head(DANE_PREVIEW_WIERSZY).to_csv(index=False)
    prompt = f"""Jesteś analitykiem danych. Dane są między znacznikami <dane_uzytkownika>.
    <dane_uzytkownika>
    {dane_csv}
    /dane_uzytkownika>
    Napisz narracyjny raport po polsku, w Markdown."""
    return prompt

def stworz_wykres(df):
    kolumny_liczbowe = df.select_dtypes(include="number").columns
    if len(kolumny_liczbowe) == 0:
        return None
    kolumna = kolumny_liczbowe[0]
    plt.figure(figsize=(8, 4))
    df[kolumna].hist(bins=20, color="#0097e6", edgecolor="white")
    plt.title(f"Rozkład wartości: {kolumna}")
    plt.tight_layout()
    bufor = io.BytesIO()
    plt.savefig(bufor, format="png")
    plt.close()
    bufor.seek(0)
    return base64.b64encode(bufor.read()).decode("utf-8")

def zapisz_raport_html(tresc_markdown, nazwa_pliku, nazwa_zrodlowa, wykres_base64):
    tresc_html = md_lib.markdown(tresc_markdown)
    sekcja_wykresu = ""
    if wykres_base64:
        sekcja_wykresu = f'<img src="data:image/png;base64,{wykres_base64}">'
    szablon = f"""<html><body>{sekcja_wykresu}<div>{tresc_html} </div> </body> </html>"""
    folder_raportow = os.path.join("static", "raporty")
    os.makedirs(folder_raportow, exist_ok=True)
    sciezka = os.path.join(folder_raportow, nazwa_pliku)
    with open(sciezka, "w", encoding="utf-8") as plik_html:
        plik_html.write(szablon)
    return f"/static/raporty/{nazwa_pliku}"

@app.route("/")
def strona_glowna():
    return render_template("index.html", odpowiedz=None)

@app.route("/rejestracja", methods=["GET", "POST"])
def rejestracja():
    if request.method == "GET":
        return render_template("rejestracja.html")
    nazwa_uzytkownika = request.form.get("nazwa_uzytkownika", "").strip()
    haslo = request.form.get("haslo", "")
    if nazwa_uzytkownika == "" or haslo == "":
        return render_template("rejestracja.html", blad="Wypełnij oba pola.")
    if len(haslo) < 8:
        return render_template("rejestracja.html", blad="Min. 8 znaków.")
    uzytkownicy = wczytaj_uzytkownikow()
    if nazwa_uzytkownika in uzytkownicy:
        return render_template("rejestracja.html", blad="Zajęta nazwa.")
    haslo_hash = bcrypt.generate_password_hash(haslo).decode("utf-8")
    uzytkownicy[nazwa_uzytkownika] = {"haslo_hash": haslo_hash}
    zapisz_uzytkownikow(uzytkownicy)
    return render_template("rejestracja.html", sukces="Konto utworzone!")

@app.route("/logowanie", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def logowanie():
    if request.method == "GET":
        return render_template("logowanie.html")
    nazwa_uzytkownika = request.form.get("nazwa_uzytkownika", "").strip()
    haslo = request.form.get("haslo", "")
    uzytkownicy = wczytaj_uzytkownikow()
    dane_uzytkownika = uzytkownicy.get(nazwa_uzytkownika)
    if dane_uzytkownika is None or not bcrypt.check_password_hash(
    dane_uzytkownika["haslo_hash"], haslo
    ):
        return render_template("logowanie.html", blad="Błędne dane.")
    session["nazwa_uzytkownika"] = nazwa_uzytkownika
    return redirect(url_for("strona_glowna"))

@app.route("/wyloguj")
def wyloguj():
    session.pop("nazwa_uzytkownika", None)
    return redirect(url_for("logowanie"))

@app.route("/zapytaj", methods=["POST"])
@limiter.limit("10 per minute")
@wymaga_logowania
def zapytaj():
    tresc_pytania = request.form.get("pytanie", "").strip()
    if tresc_pytania == "":
        return render_template("index.html", odpowiedz="Wpisz pytanie!")
    tresc_pytania = oczysc_tekst(tresc_pytania)
    if len(tresc_pytania) > MAX_DLUGOSC_PYTANIA:
        return render_template("index.html", odpowiedz="Za długie.")
    if wyglada_na_probe_injection(tresc_pytania):
        return render_template("index.html", odpowiedz="Podejrzana treść.")
    odpowiedz = zapytaj_claude(tresc_pytania, system_prompt=SYSTEM_PROMPT_CZAT)
    odpowiedz = waliduj_output(odpowiedz)
    return render_template("index.html", odpowiedz=odpowiedz)

@app.route("/analiza-strona")
def analiza_strona():
    return render_template("analiza.html")

@app.route("/analizuj", methods=["POST"])
@limiter.limit("5 per minute")
@wymaga_logowania
def analizuj():
    plik = request.files.get("plik_csv")
    if not plik or plik.filename == "":
        return render_template("analiza.html", blad="Nie wybrano pliku.")
    if not plik.filename.endswith(".csv"):
        return render_template("analiza.html", blad="Prześlij .csv.")
    try:
        df = pd.read_csv(plik)
    except Exception as e:
        return render_template("analiza.html", blad=f"Błąd: {e}")
    if len(df) > MAX_WIERSZY_CSV:
        return render_template("analiza.html", blad="Za duży plik.")

    liczba_wierszy, liczba_kolumn = df.shape
    prompt = zbuduj_prompt_analizy(df)
    podsumowanie = zapytaj_claude(prompt)
    nazwa_bezpieczna = secure_filename(plik.filename)
    nazwa_raportu = f"raport_{os.path.splitext(nazwa_bezpieczna)[0]}.html"
    wykres_base64 = stworz_wykres(df)
    link_do_raportu = zapisz_raport_html(
        podsumowanie, nazwa_raportu, plik.filename, wykres_base64
    )
    return render_template(
    "analiza.html", nazwa_pliku=plik.filename,
    liczba_wierszy=liczba_wierszy, liczba_kolumn=liczba_kolumn,
    podsumowanie_ai=podsumowanie, link_do_raportu=link_do_raportu,
    )

@app.route("/polityka-prywatnosci")
def polityka_prywatnosci():
    return render_template("polityka_prywatnosci.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)