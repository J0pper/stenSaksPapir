import random

muligeSvar = ["sten", "saks", "papir"]
computerSvar = random.choice(muligeSvar)
#print(computerSvar)
brugerSvar = input('Sten saks papir?')

#prints the computers and the users choice
print('Du valgte', brugerSvar, "computeren valgte", computerSvar)

#checks if you won or lost
if computerSvar == brugerSvar:
    print('BRUH')

elif computerSvar == "sten":
    if brugerSvar == "papir":
        print('YOU WIN')

    else:
        print('YOU LOSE BOHOOO')

elif computerSvar == "papir":
    if brugerSvar == "saks":
        print('YOU WON')

    else:
        print('YOU LOSE')

elif computerSvar == "saks":
    if brugerSvar == "sten":
        print('YOU WON')

    else:
        print('YOU LOSE')