# pojistenci_operations.py
from pojisteny import Pojisteny

def pridat_noveho_pojistence(list_pojistencu):
    # Ввод имени
    while True:
        jmeno = input("Zadejte jméno pojisteného: ").strip()
        if not jmeno or not jmeno.isalpha():
            print("Jméno nesmí být prázdné a musí obsahovat pouze písmena.")
        else:
            break

    # Ввод фамилии
    while True:
        prijmeni = input("Zadejte přijméní pojisteného: ").strip()
        if not prijmeni or not prijmeni.isalpha():
            print("Přijméní nesmí být prázdné a musí obsahовать pouze písmena.")
        else:
            break

    # Ввод возраста
    while True:
        vek = input("Zadejte vek pojisteného: ").strip()
        if not vek.isdigit():
            print("Věk musí být číslo.")
            continue
        vek_digit = int(vek)
        if not 130 > vek_digit > 0:
            print("Věk musí být v rozmezí od 1 do 130 let.")
        else:
            break
    # Ввод телефона
    telefon = input("Zadejte telefon pojisteného: ").strip()

    # Создание объекта Pojisteny
    pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)

    # Добавление объекта в список
    list_pojistencu.append(pojisteny)
    print("Pojištěný byl úspěšně přidán.")
