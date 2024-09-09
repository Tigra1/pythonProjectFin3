from pojisteny import Pojisteny
from menu import Menu
class Formular:
    print("--------------------")
    print("Evidence pojištenych")
    print("--------------------")
    list_pojistencu = []
    pokracovat = "ano"
    while pokracovat.lower() == "ano":
        Menu()
        volba = int(input())
        match volba:
            case 1:
                print()
                # Vytvoření pojišteného

                jmeno = input("Zadejte jméno pojisteného: ").strip()
                prijmeni = input("Zadejte přijméní pojisteného: ").strip()
                # if prijmeni == None:
                # raise Exception("Položka přijméní je povinná a nesmí být prázdná.")

                vek = int(input("Zadejte vek pojisteného: ").strip())

                telefon = input("Zadejte telefon pojisteného: ").strip()
                pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
                list_pojistencu.append(pojisteny)
                print("Pojištěný byl úspěšně přidán.")
            case 2:
                if list_pojistencu:
                    print("\nSeznam všech pojištěných:")
                    for pojisteny in list_pojistencu:
                        print(pojisteny)
                else:
                    print("Žádní pojištěnci nejsou v evidenci.")
            case 3:
                # Vyhledání pojištěného
                hledane_jmeno = input("Zadejte jméno nebo přijmení pro vyhledání: ").strip()
                nalezeni = False

                for pojisteny in list_pojistencu:
                    if pojisteny.jmeno.lower() == hledane_jmeno.lower() or pojisteny.prijmeni.lower() == hledane_jmeno.lower():
                        print(pojisteny)
                        nalezeni = True

                if not nalezeni:
                    print("Pojištěný s tímto jménem nebo přijmením nebyl nalezen.")

            case 4:
                print("Děkuji za použití aplikaci.")
        if volba != 4:
            pokracovat = input("Přejete si zadat další příklad? [ano/ne]: ")
        else:
            break