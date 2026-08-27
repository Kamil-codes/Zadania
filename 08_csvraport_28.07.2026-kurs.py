import pandas as pd

df = pd.read_csv("sprzedaz.csv")

top5produktow=df.groupby("produkt")["ilosc_zamowien"].sum().sort_values(ascending=False).head(5)
srednia_zamowien_produktow= df.groupby("produkt")["wartosc"].mean()
miesięczne_sumy = df.groupby("miesiac")[["wartosc", "ilosc_zamowien"]].sum()

top5produktow.to_csv("top5produktow.csv", index=False)
srednia_zamowien_produktow.to_csv("srednia_zamowien.csv", index=False)
miesięczne_sumy.to_csv("miesieczne_sumy.csv", index=False)