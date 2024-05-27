from novy_pojisteny import NovyPojisteny
from sprava_pojisteni import SpravaPojisteni


class SpravaAplikace:
#metoda bude využita jinou metodou, metoda získá vstup a ověří, že není prázdný, ořízne od bílých znaků
    @staticmethod
    def nacti_udaj(zprava):
        while True:
            udaj = input(zprava)
            if udaj.strip():
                return udaj
            print("Hodnota nesmí být prázdná.")

#metoda bude využita jinou metodou, metoda získá vstup a ověří, že není prázdný, a že se jedná o číslo, ořízne od bílých znaků
    @staticmethod
    def nacti_cislo(zprava):
        while True:
            try:
                udaj = input(zprava)
                if not udaj.strip():
                    print("Hodnota nesmí být prázdná")
                    continue
                udaj = int(udaj)
                return udaj
            except ValueError:
                print("Hodnota musí být číslo")

#metoda vrátí zadané údaje k uložení do seznamu pojištěných, v případě jména a příjmení zajistí, že první písmeno bude velké
    def pridej_pojisteneho(self):
        jmeno = SpravaAplikace.nacti_udaj("Zadejte jméno:\n").capitalize()
        prijmeni = SpravaAplikace.nacti_udaj("Zadejte příjmení:\n").capitalize()
        tel_cislo = SpravaAplikace.nacti_udaj("Zadejte telefonní číslo:\n")
        vek = SpravaAplikace.nacti_cislo("Zadejte věk:\n")

        return NovyPojisteny(jmeno, prijmeni, tel_cislo, vek)

#metoda vypíše pojistěného ze seznamu pojištěných pokud v něm je, v opačném případě vypíše "Pojištěný nenalezen"
    def zobraz_pojisteneho(self,pojisteny):
        if pojisteny:
            print(pojisteny)
        else:
            print("Pojistěný nenalezen")

#metoda slouží k ukončení jednoho kroku
    @staticmethod
    def pokracovat():
        input("Pokračujte libovolnou klávesou...")
        print()

#metoda zobrazí volby před každým výběrem
    @staticmethod
    def zobraz_zahlavi():
        print("""
----------------------------------------------------------------
                    Evidence pojištěných
----------------------------------------------------------------
""")

        print("Vyberte akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")
        (print
("""
----------------------------------------------------------------
"""))

