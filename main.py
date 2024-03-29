import random
import time


import pygame

from Circle import circleClass

pygame.init()

game_window_width = pygame.display.Info().current_w
game_window_height = pygame.display.Info().current_h
screen = pygame.display.set_mode([game_window_width, game_window_height])


def layout():
    screen.fill((217, 209, 198))

    pygame.draw.rect(screen, (78, 78, 85), pygame.Rect(0, 200, game_window_width, 400))

    pygame.draw.circle(screen, (0, 0, 0), (game_window_width / 3, game_window_height - 100), 50)
    pygame.draw.circle(screen, (0, 0, 0), (game_window_width / 2, game_window_height - 100), 50)
    pygame.draw.circle(screen, (0, 0, 0), (game_window_width * 2/3, game_window_height - 100), 50)

    sten_billede = pygame.image.load('sten_gesture.png')
    sten_billede = pygame.transform.scale(sten_billede, (75, 75))
    screen.blit(sten_billede, (game_window_width / 3 - 75 / 2, (game_window_height - 100) - 75 / 2))

    saks_billede = pygame.image.load('saks_gesture.png')
    saks_billede = pygame.transform.scale(saks_billede, (75, 75))
    screen.blit(saks_billede, (game_window_width / 2 - 75 / 2, (game_window_height - 100) - 75 / 2))

    papir_billede = pygame.image.load('papir_gesture.png')
    papir_billede = pygame.transform.scale(papir_billede, (75, 75))
    screen.blit(papir_billede, (game_window_width * 2/3 - 75 / 2, (game_window_height - 100) - 75 / 2))


    

def whatchuClicking(xPos, yPos, width, height):
    mouse = pygame.mouse.get_pos()
    xMouse = mouse[0]
    yMouse = mouse[1]

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gameWindowWidth / 2 - 75 <= mouse[0] <= gameWindowWidth / 2 + 75 and gameWindowHeight / 2 - 75 <= mouse[1] <= gameWindowHeight / 2 + 75:
                pygame.quit()



running = True

while running:
    layout()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False


    pygame.display.update()

'''

running = True
while running:
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
        afslut = ["", "dø"]
        spil_igen = input("Tryk enter for at spille igen eller skriv dø for at afslutte spillet").lower()

        if not spil_igen in afslut:
            print(f"{spil_igen} er ikke et gyldigt svar, prøv igen!")

        else:
            if spil_igen == "dø":
                running = False
                break
            elif spil_igen == "":
                break

print("hvor er du kedelig!")


'''