import sys

print()  # wypisz/wydrukuj

print("Radek")
print('Radek')
# Radek
# Radek

# ctrl / - komentarz
# print('Radek")
#   File "C:\Users\CSComarch\PycharmProjects\PythonAnalizaDanych28-07-2025A\pierwszy.py", line 7
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 7)
# Process finished with exit code 1
print("dalsza część")  # <class 'str'> - teksty

print(type("Radek"))
print("39" + "14")  # 3914 łaczenie tekstów, konkatenacja tekstów

print(39 + 14)  # 53

# print("39" + 14)  # TypeError: can only concatenate str (not "int") to str

print(type(34))  # <class 'int'>, liczba całkowita
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# zmienna - pudełko na dane

name = "Radek"
print(name)  # Radek
# snake_case
# kebab-case
# PascalCase -> UpperCamelCase

# typowanie dynamiczne
name = "Radek"
print(type(name))  # <class 'str'>
name = 67
print(name)
print(type(name))  # <class 'int'>

age = 48
print(age)
print(type(age))

print(10 * "45")  # 45454545454545454545

# podpowiedzi typów
name: str = 90
# mypy sprawdza typy w kodzie
# pip install mypy
# mypy .\pierwszy.py
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonAnalizaDanych28-07-2025A> mypy .\pierwszy.py
# pierwszy.py:44: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:55: error: Name "name" already defined on line 35  [no-redef]
# Found 2 errors in 1 file (checked 1 source file)

tekst = "Witaj Świecie"

print(tekst)
print(type(tekst))

# """ Return a copy of the string converted to uppercase. """
# teksty sa niemutowalne
tekst.upper()
print(tekst)  # Witaj Świecie
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_zmienna = tekst.upper()
print(tekst_zmienna)

zmienna1 = "GROSS"
zmienna2 = "groß"

print(zmienna1.lower() == zmienna2.lower())  # False
print(zmienna1.casefold() == zmienna2.casefold())  # True
# == porównanie

print(1 != 8)  # rózne, True

print(bool(1))  # True

print(int(True))  # 1

print(bool("Radek"))  # True
# None - odpowiednik null, nie wiem, stan nieokreslony

temp = 36.6  # zmmiennoprzecinkowe
print(type(temp))  # <class 'float'>
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)


print(0.1 + 0.9)  # 1.0
print(0.1 + 0.2)  # 0.30000000000000004

# f - string - sformatowany tekst
name = "Radek"
print(f"Nazywam się {name}")

liczba = 3.90001
print(f"Wersja pythona: {liczba:.2f}")  # Wersja pythona: 3.90

print(100 / 3)  # dzielenie
print(100 // 3)  # dzielenie bez reszty, czesc całkowita dzielenia
print(100 % 3)  # modulo - reszta z dzielenia

zysk = 567876543123
print(f"Nasza duża liczba: {zysk:,}")  # Nasza duża liczba: 567,876,543,123
# ctrl d powielenie lini
print(f"Nasza duża liczba: {zysk:_}")  # Nasza duża liczba: 567_876_543_123
print(f"Nasza duża liczba: {zysk:_}".replace("_", " "))  # Nasza duża liczba: Nasza duża liczba: 567 876 543 123

parametr = 1_000_000_000
print(parametr)  # 1000000000
print(type(parametr))  # <class 'int'>
