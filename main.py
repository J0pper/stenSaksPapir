import random
import time

muligeSvar = ["sten", "saks", "papir"]
computerSvar = random.choice(muligeSvar)


print("Er du klar på et spil STEN SAKS PAPIR!?!")
while True:
    brugerSvar = input('Skriv dit valg her:').lower()

    if not brugerSvar in muligeSvar:
        print(f"{brugerSvar} er ikke en mulighed... try again mate")

    else:
        break

print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)

print(f"Du valgte {brugerSvar} og computeren valgte {computerSvar}")
brugerindex = muligeSvar.index(brugerSvar)
compindex = muligeSvar.index(computerSvar)

if brugerindex == compindex:
    print("bruh... draw -_-")

if brugerindex != 0:
    if brugerindex < compindex:
        print("WOW du vandt!")

    elif brugerindex > compindex:
        print("ØV, du tabte, prøv igen :/")

elif brugerindex == 0:
    if compindex == 1:
        print("u win!!!")

    elif compindex == 2:
        print("u lose xDDDDD")