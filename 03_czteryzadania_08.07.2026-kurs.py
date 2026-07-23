import math
# zadanie 1
exam_points = {"Mariusz":30, "Mateusz":55, "Marta":76, "Roman":30,
    "Arleta":59, "Adrian":96, "Monika":91, "Andrzej":22,
    "Krzysztof":83, "Krystyna":93, "Piotr":44, "Dawid":10, "Agnieszka":15}
# skala: 0-45 ndst | 46-60 dop | 61-75 dst | 76-90 db | 91-100 bdb
maksymalnepunkty=0
failed_students = []
top_students = []
best_student = None
for imie, punkt in exam_points.items():
    if punkt <= 45:
        failed_students.append(imie)
    elif punkt >=91: 
        top_students.append(imie)
    if punkt > maksymalnepunkty:
        maksymalnepunkty=punkt
        best_student = (imie, punkt)
#zadanie 2
names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz',
'Edward', 'Piotr', 'Jan', 'Denis', 'Amir', 'Igor', 'Borys',
'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel']
name_dict = {}
for imie in names:
    name_dict.setdefault(imie[0], set())
    name_dict[imie[0]].add(imie)
print(name_dict) #sprawdzenie
#zadanie 3
num = 30
fibonacci = []
while len(fibonacci) < num:
    if len(fibonacci) == 0 or len(fibonacci) == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(sum(fibonacci[-2:]))
print(fibonacci)#sprawdzenie
#zadanie 4
def equation(a, b, c):
    delta = b**2-4*a*c
    if delta < 0:
        return ("Brak rozwiązań")
    elif delta == 0:
        x0=-b/(2*a)
        return (x0)
    elif delta > 0:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        return(x1, x2)