#dodac inputa
#sprawdzic czy podano LICZBE z zakresu 1-3
#przypisac liczby do obiektu
#wygenerowac losowo co daje przeciwnik
#porównac wyniki
#wyznaczyć czy wygrałem przegrałem czy zremisowałem
#dac informacje zwrotną
slownik = {1: "kamień", 2: "Papier", 3:"nożyce"}
import random
def correct():
    if choose == 1 or choose == 2 or choose == 3:
        return True
    else: return False

def win():
    if choose == 1 and enemy_choose == 3 or choose ==  2 and enemy_choose == 1 or choose == 3 and enemy_choose == 2:
        return True
    else: return False
def loose():
    if choose == 3 and enemy_choose == 1 or choose == 1 and enemy_choose == 2 or choose == 2 and enemy_choose == 3:
        return True
    else: return False



while True:
    enemy_choose = random.randint(1,3)
    try:
        choose = int(input("Witam oto gra papier, kamień, nożyce. Wybierz liczbe od 1-3 \n1.Kamień\n2.Papier\n3.Nożyce \nCo wybierasz?: "))
    except:
        print("To nie liczba!")
        continue
    if not correct():
        print("nie podałes liczby z zakresu 1-3.")
        continue
    else:

        if win():

            print("WYGRAŁEŚ :) \nWybór przeciwnika: ", slownik[enemy_choose], "\nTwój wybór: ", slownik[choose] )
        elif loose():

            print("Przegrałeś :( \nWybór przeciwnika: ", slownik[enemy_choose], "\nTwój wybór: ", slownik[choose])
        else:

            print("Remis! \nWybór przeciwnika: ", slownik[enemy_choose], "\nTwój wybór: ", slownik[choose])






