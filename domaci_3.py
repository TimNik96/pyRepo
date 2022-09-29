# - Napraviti niz od 50 nasumicnih brojeva od 0 do 100 (koristeci randint funkciju). Nakon toga odrediti broj parnih I broj neparnih brojeva I to ispisati.

    # from random import randint

    # lista_nasumicnih = []
    # broj_parnih = 0
    # broj_neparnih = 0

    # while len(lista_nasumicnih) < 50:
    #     lista_nasumicnih.append(randint(0,100))

    # for broj in lista_nasumicnih:
    #     if broj % 2 == 0:
    #         broj_parnih += 1
    #     else:
    #         broj_neparnih += 1

    # print(broj_parnih, broj_neparnih)

# - Napraviti program koji ima unos broja, nakon toga on stampa svaku cifru unetog broja jednu ispod druge.

    # broj = input('Unesite broj: ')

    # for cifre in broj:
    #     print(cifre)

# - Napraviti program koji ima sledecu stampu, na osnovnu unesenog broja ako je uneseni broj 4.

    # *
    # **
    # ***
    # ****
    # ***
    # **
    # *

    # visina_figure = eval(input("Unesite visinu figure: "))

    # for i in range(1, visina_figure * 2):
    #     if i <= visina_figure:
    #         print('*' * i)
    #     else:
    #         print('*' * (visina_figure * 2 - i))

# - Napraviti program u kom se unosi broj bodova sve dok se ne unese vrednost
#   manja od 0 ili veca od 100, sve ispravne unete vrednosti dodati u listu,
#   kada se unesu neispravne vrednosti izracunati prosek i izracunati koliko
#   je desetki bilo na ispitu, granica za 10 je sve vise od 90 bodova na kraju ispisati prosek i broj desetki.

    # from math import *

    # lista_bodova = []
    # bodovi = 0
    # broj_desetki = 0
    # prosek = 0

    # while True:
    #     bodovi = eval(input('Unesite broj bodova sa ispita: '))
    #     if bodovi < 0 or bodovi > 100:
    #         break
    #     elif bodovi < 51:
    #         print('Broj bodova nije validan za prolaznu ocenu!')
    #     else:
    #         lista_bodova.append(bodovi)

    # for ocena in lista_bodova:
    #     if ocena >= 90:
    #         broj_desetki += 1
        
    #     if ocena == 100:
    #         prosek += 10
    #     else:
    #         prosek += floor(ocena / 10) + 1

    # print("Broj desetki: ", broj_desetki)
    # print(prosek/len(lista_bodova))
