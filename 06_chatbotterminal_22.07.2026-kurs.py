import os
from dotenv import load_dotenv
from anthropic import (
    Anthropic,
    RateLimitError,
    APIConnectionError,
    AuthenticationError,
    APIError,
    )


load_dotenv()

client = Anthropic(api_key = os.environ.get("ANTHROPIC_API_KEY"))

historia=[]

def zapiszwpliku(nazwa_pliku="rozmowa.txt"):
    """Zapisuje całą historię rozmowy do pliku tekstowego."""
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        for wpis in historia:
            kto = "Ty" if wpis["role"] == "user" else "Claude"
            plik.write(f"{kto}: {wpis['content']}\n\n")

print("By zakończyć rozmowę napisz 'quit'")

while True:
    odp=input("\nTy:")
    if odp.lower()=="quit":
        zapiszwpliku()
        print("\n Do widzenia!")
        break
    if odp.strip() == "":
        print("Napisz coś do Chatbotu AI")
        continue
    historia.append({
        "role": "user",
        "content": odp
    })
    try:
        wiadomosc = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            messages= historia
        )
        odpowiedz=wiadomosc.content[0].text
        print("\nClaude: ", odpowiedz)
        historia.append({
            "role": "assistant", 
            "content": odpowiedz
            })  
    except AuthenticationError:
        historia.pop()
        print ("BŁĄD: nieprawidłowy klucz API.")
    except RateLimitError:
        historia.pop()
        print ("BŁĄD: zbyt wiele zapytań.")
    except APIConnectionError:
        historia.pop()
        print ("BŁĄD: problem z połączeniem.")
    except APIError as blad:
        historia.pop()
        print (f"BŁĄD: coś poszło nie tak ({blad}).")
