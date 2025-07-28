# # kolekcje - przechowuje wiele elemntów, rożnego typu na raz
#
# # lista - zachowuje kolejnosc prtzy dodawaniu elemntów
# lista = []
# print(type(lista))  # <class 'list'>
# lista.append('Radek')
# print(lista)  # ['Radek']
#
# # krotka - tuple - kolekcja niemutowalna, tylko do odczytu
# # pozwala lepiej zarządzac pamięcią
# krotka = 23, 34, 54, "Radek"
# print(krotka)  # (23, 34, 54, 'Radek')
#
# print(len(krotka))  # 4 długosc krotki
#
# # zbiór - set() - przechowujue unikalne wartość
# # nie posiada indeksu, nie zachowuje kolejnosc
# lista1 = [2, 4, 5, 6, 7, 8, 9, 9, 10, 2, 3]
# zbior = set(lista1)
# print(zbior)  # {2, 3, 4, 5, 6, 7, 8, 9, 10}
# zbior.add("Tomek")
# print(zbior)  # {'Tomek', 2, 3, 4, 5, 6, 7, 8, 9, 10}
# zbior2 = {2, 3, 4, 5, 6, 7}
# print(zbior.difference(zbior2))  # {8, 9, 10, 'Tomek'}
# pusty_zbior = set()
# print(pusty_zbior)  # set() - pusty zbior
# matrix = [[3, 4, 5], [6, 7, 8]]
# print(matrix)  #
#
# print(matrix[0])  # [3, 4, 5]
# print(matrix[0][0])  # 3
#
# print(6 in zbior)  # True
# print(6 in lista1)  # True
#
# imie = input("Jak masz na imię?")  # zwraca str
# print(imie)
# print(type(imie))
# # Jak masz na imię?radek
# # radek
# # <class 'str'>
# try:
#     a = int(input("Podaj pierwszą liczbę"))
#     b = input("Podaj drugą liczbę")
#
#     # print(int(a) + float(b))
#     wynik = int(a) + float(b)
# except ValueError:
#     print("Bład wartości")
# except TypeError:
#     print("Błąd typu")
# except Exception as e:
#     print("Błąd:", e)
# else:  # tylko gdy nie ma błedu
#     print("Wynik działania:", wynik)
# finally:  # wykona się zawsze
#     print("kolejne działanie")
# # Podaj pierwszą liczbę1
# # Podaj drugą liczbę2
# # 3
#
# for liczba in range(3):  # 0,1,2
#     print(liczba)
#
# print("Poza pętlą")
# # 0
# # 1
# # 2
# # Poza pętlą
#
# # Pętla sterowana warunkiem
# while True:
#     print("Na jakim kursie jeste?")
#     wybor = input()
#     if wybor == 'java':
#         break  # przerywa petle
#     print("Ok")
#
# print('Koniec pętli')
# # Ok
# # Na jakim kursie jeste?
# # 3
# # Ok
# # Na jakim kursie jeste?
# # java
# # Koniec pętli
# i = 0
# while i < 3:
#     print(i)
#     i += 1
# # 0
# # 1
# # 2

osoba = ['Radek', "Tomek", "Anna", 'Marek', 'Zenek']
wiek = [44, 55, 56, 89]

# Radek 44
# zip()
for i in zip(osoba, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Anna', 56)
# ('Marek', 89)

# rozpakowanie krotki
a, b = ('Radek', 44)
print(a, b)  # Radek 44
for o, w in zip(osoba, wiek):
    print(o, w)
# Radek 44
# Tomek 55
# Anna 56
# Marek 89

# 0 Radek 44
lista_liczb = [9, 99, 99]
print(tuple(enumerate(lista_liczb)))
# ((0, 9), (1, 99), (2, 99))

for i in enumerate(zip(osoba, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Anna', 56))
# (3, ('Marek', 89))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(c, d)
a, (c, d) = (1, ('Tomek', 55))
print(a, c, d)  # 1 Tomek 55
for i, (o, w) in enumerate(zip(osoba, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Anna 56
# 3 Marek 89
for i, (o, w) in enumerate(zip(osoba, wiek), start=1):
    print(i, o, w)
    # 1 Radek 44
    # 2 Tomek 55
    # 3 Anna 56
    # 4 Marek 89
