from sprava_pojisteni import SpravaPojisteni
from sprava_aplikace import SpravaAplikace

#vytvoření instance třídy SpravaPojisteni a SpravaAplikace
sprava_P = SpravaPojisteni()
sprava_A = SpravaAplikace()

#cyklus pro uživatelskou volbu, na začátku se vždy zobrazí výpis voleb
while True:
    sprava_A.zobraz_zahlavi()

#ošetření, že volba bude číslo
    try:
        volba = int(input("Vyberte možnost:\n"))
    except ValueError:
        print("Neplatná volba. Zadejte číslo.")
        input("Pokračujte libovolnou klávesou...")
        continue

#jednotlivé volby, které využívají definované metody
    if volba == 1:
        pojisteny = sprava_A.pridej_pojisteneho()
        sprava_P.pridat(pojisteny)
        sprava_A.pokracovat()

    elif volba == 2:
        sprava_P.vypis_vsechny()
        sprava_A.pokracovat()

    elif volba == 3:
        jmeno = sprava_A.nacti_udaj("Zadejte jméno:\n").strip()
        prijmeni = sprava_A.nacti_udaj("Zadejte příjmení:\n").strip()
        pojisteny = sprava_P.vyhledej(jmeno, prijmeni)
        sprava_A.zobraz_pojisteneho(pojisteny)
        sprava_A.pokracovat()

    elif volba == 4:
        print("Děkujeme, že jste využili naše služby.")
        print("Nashledanou!")
        break
#"Neplatná volba" v případě, že uživatel zvolí číslo jiné než 1-4.
    else:
        print("Neplatná volba")
        sprava_A.pokracovat()

