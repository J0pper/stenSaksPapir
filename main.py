import random
import time
def sten_saks_papir():
    #Opsætter liste med alle mulige svar i spillet sten, saks og papir.
    mulige_svar = ["sten", "saks", "papir"]

    #Variabel der vælger en tilfældig valgmulighed i listen med mulige svar.
    computer_svar = random.choice(mulige_svar)

    #Dictionary over hvilke træk, der vinder over hianden.
    hvem_vinder = {"sten":"saks", "saks":"papir", "papir":"sten"}

    print("Er du klar på et spil STEN SAKS PAPIR!?!")
    time.sleep(1)
    print("Sten")
    time.sleep(1)
    print("Saks")
    time.sleep(1)
    print("Papir")
    time.sleep(1)
    print("NU")

    #Beder brugeren om et input. Tjekker om det indgår i listen med mulige svar, hvis ikke spørger den igen.
    while True:
        bruger_svar = input('Skriv dit valg her:').lower()

        if not bruger_svar in mulige_svar:
            print(f"{bruger_svar} er ikke en mulighed... try again mate")

        else:
            break


    #SUSPENSE!!!!
    time.sleep(1)
    #Variabel der forklarer, hvad brugeren og computeren valgte. Bruges senere til at placere valgene samt resultatet på samme linje.
    forskellige_valg = f"Du valgte {bruger_svar} og computeren valgte {computer_svar}"

    #Tjekker om brugerens svar er det samme som computerens. Hvis ja er spillet uafgjort.
    if bruger_svar == computer_svar:
        print(f"{forskellige_valg}."" bruh... draw -_-")

    #Tilgår et dictionary over hvilke træk der slår hvad med en key suppleret af brugeren gennem input.
    #Hvis valuen der tillægger sig keyen er ens med computerens svar, har brugeren vundet.
    elif hvem_vinder[bruger_svar] == computer_svar:
        print(f"{forskellige_valg}."" WOHOOOO DU VINDER")

    #Tilgår et dictionary over hvilke træk der slår hvad, med en key suppleret af computeren gennem random choice.
    #Hvis valuen der tillægger sig keyen er ens med brugerens svar, har brugeren vundet.
    elif hvem_vinder[computer_svar] == bruger_svar:
        print(f"{forskellige_valg}."" BOHOOOO DU TABER")


    #Spørger brugeren om de vil spille videre eller afslutte spillet.
    while True:
        spil_igen = input("Tryk enter for at spille igen eller skriv dø for at afslutte spillet")
        if spil_igen == "":
            sten_saks_papir()

        elif spil_igen == "dø":
            break

        else:
            print(f"{spil_igen} er ikke et gyldigt svar, prøv igen!")

    print("hvor er du kedelig!")

sten_saks_papir()