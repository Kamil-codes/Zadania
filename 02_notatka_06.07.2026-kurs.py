import json
with open("notatki.json", "r", encoding="utf-8") as file:
    plik = file.read()
if plik == "":
    wartosc = []
else:
    wartosc=json.loads(plik)
while True:
    action=input(" 1-dodawać notatki,\n 2-wyświetlać listę,\n 3-usuwać wybrane notatkit,\n kliknij dowolny klawisz, aby zakończyć proces\n")
    match action:
        case "1":
            slowo=input("napisz coś")
            wartosc.append(slowo)
            with open("notatki.json", "w", encoding="utf-8") as file:
                json.dump(wartosc, file, ensure_ascii=False, indent=4)
        case "2":
            for liczba, notatka in enumerate(wartosc):
                print(liczba," ",notatka)
        case "3":
            box=int(input("co chcesz usunąć z listy (pamiętaj że pierwsze od góry jest liczone jako 0)"))
            if 0<=box<len(wartosc):
                wartosc.pop(box)
                with open("notatki.json", "w", encoding="utf-8") as file:
                    json.dump(wartosc, file, ensure_ascii=False, indent=4)
            else:
                print("Eror lub nie ma takiej notatki")
        case _:
            break
#założyłem że plik json jest pusty i sam kod nie tworzy takiego pliku