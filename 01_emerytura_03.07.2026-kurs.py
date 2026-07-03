imie = input("Jakie masz imie? ") # zadaniu pisze że pyta użytkownika a tego nie ma w programię, więc dlatego użyłem input
lat = int(input("Ile masz lat? ")) # zrobiłem int by nieinterpretował mi tego tekst a liczbę
ile = 60 - lat #przyjełem że emerytura przysługuje kiedy ma się 60 lat
print (f"Witaj {imie}. Masz {lat} lat i pozostało ci do emerytury {ile} lat.")