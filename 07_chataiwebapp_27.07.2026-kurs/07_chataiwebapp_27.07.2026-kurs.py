import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from anthropic import (
    Anthropic,
    RateLimitError,
    APIConnectionError,
    AuthenticationError,
    APIError,
)
load_dotenv()
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

MODEL = "claude-haiku-5"
MAX_TOKENS = 200
app = Flask(__name__)

def zapytaj_claude(tresc_pytania, styl):
    if styl == "0":
        system_prompt = "Odpowiadaj standardowo lub zwykle i pomocniej."
    elif styl == "1":
        system_prompt = "Odpowiadaj krótko i konkretnie."
    elif styl == "2":
            system_prompt = "Odpowiadaj długo i szczególowo wraz z wyjaśnieniem i przykładem."
    elif styl == "3":
            system_prompt = "Odpowiadaj jak ekspertem danej dziedzinie i znał się na wszystkim. Używaj języka profesjonalnego."
    elif styl == "4":
            system_prompt = "Odpowiadaj jak nauczyciel. Wyjaśniaj krok po kroku, czyli aż użytkownik zrozumie to czego chce wiedzieć."
    else:
        system_prompt = "Brak ustawionego promptu"

    try:
        odpowiedz = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system_prompt,
        messages=[{"role": "user", "content": tresc_pytania}],
        )
        return odpowiedz.content[0].text
    except AuthenticationError:
        return "BŁĄD: nieprawidłowy klucz API."
    except RateLimitError:
        return "BŁĄD: zbyt wiele zapytań. Spróbuj za chwilę."
    except APIConnectionError:
        return "BŁĄD: problem z połączeniem internetowym."
    except APIError as blad:
        return f"BŁĄD: {blad}"

@app.route("/")
def strona_glowna():
    return render_template("04_htmlformularz_13.07.2026-kurs.html", odpowiedz=None)

@app.route("/zapytaj", methods=["POST"])
def zapytaj():
    tresc_pytania = request.form.get("text", "").strip()
    styl = request.form.get("styl", "")
    if tresc_pytania == "":
        return render_template(
    "04_htmlformularz_13.07.2026-kurs.html", odpowiedz="Wpisz najpierw jakieś pytanie!"
    )
    odpowiedz_claude = zapytaj_claude(tresc_pytania, styl)
    return render_template(
    "04_htmlformularz_13.07.2026-kurs.html", odpowiedz=odpowiedz_claude, pytanie=tresc_pytania
    )


if  __name__ == "__main__":
    app.run(debug=True)

    