# kolekcje - przechowuje wiele elemntów, rożnego typu na raz

# lista - zachowuje kolejnosc prtzy dodawaniu elemntów
lista = []
print(type(lista))  # <class 'list'>
lista.append('Radek')
print(lista)  # ['Radek']

# krotka - tuple - kolekcja niemutowalna, tylko do odczytu
# pozwala lepiej zarządzac pamięcią
krotka = 23, 34, 54, "Radek"
print(krotka)  # (23, 34, 54, 'Radek')

print(len(krotka))  # 4 długosc krotki

# zbiór - set() - przechowujue unikalne wartość
# nie posiada indeksu, nie zachowuje kolejnosc
lista1 = [2, 4, 5, 6, 7, 8, 9, 9, 10, 2, 3]
zbior = set(lista1)
print(zbior)  # {2, 3, 4, 5, 6, 7, 8, 9, 10}
zbior.add("Tomek")
print(zbior)  # {'Tomek', 2, 3, 4, 5, 6, 7, 8, 9, 10}
zbior2 = {2, 3, 4, 5, 6, 7}
print(zbior.difference(zbior2))  # {8, 9, 10, 'Tomek'}
pusty_zbior = set()
print(pusty_zbior)  # set() - pusty zbior
matrix = [[3, 4, 5], [6, 7, 8]]
print(matrix)  #

print(matrix[0])  # [3, 4, 5]
print(matrix[0][0])  # 3

print(6 in zbior)  # True
print(6 in lista1)  # True

imie = input("Jak masz na imię?") # zwraca str
print(imie)
print(type(imie))
# Jak masz na imię?radek
# radek
# <class 'str'>