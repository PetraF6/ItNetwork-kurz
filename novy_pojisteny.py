
class NovyPojisteny:

#definice vstupních parametrů
    def __init__(self, jmeno, prijmeni, tel_cislo, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.tel_cislo = tel_cislo
        self.vek = vek

#vrátí textový výpis pojistěného
    def __str__(self):
        return f"{self.jmeno}    {self.prijmeni}    {self.tel_cislo}    {self.vek}"



