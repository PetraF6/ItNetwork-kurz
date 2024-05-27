from novy_pojisteny import NovyPojisteny
class SpravaPojisteni:

#vytvoření kolekce pro ukládání nových pojistěných
    def __init__(self):
        self.pojisteni = []

#metoda přidá pojistěné do seznamu pojistěných
    def pridat(self, pojisteny):
       self.pojisteni.append(pojisteny)

#metoda vypíše všechny pojistěné, které seznam obsahuje, v opačném případě vypíše "Seznam pojištěných je prázdný"
    def vypis_vsechny(self):
        if not self.pojisteni:
            print("Seznam pojištěných je prázdný")
            return
        for pojisteny in self.pojisteni:
            print(pojisteny)

#metoda vyhledá v seznamu pojistěných pojistěného dle jména a příjmení
# také zajišťuje, aby nezáleželo, že uživatel zadá malé nebo velké písmeno
    def vyhledej(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower():
                return pojisteny
        return None

