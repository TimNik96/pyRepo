# for i in range(10):
#     print("Pozdrav")

# -Napisati program koji racuna stepen unetog broja

    # osnova = eval(input("Uneti osnovu za stepenovanje: "))
    # stepen = eval(input("Uneti eksponent za stepenovanje: "))
    # rezultat = 1

    # for i in range(stepen):
    #     rezultat = rezultat * osnova

    # print(rezultat)

# -Napisati program koji vrsi odbrojavanje unazad

# for i in range(10, -1, -1):
#     print(i, end=' ')

# -Napisati program koji prevodi Celzijuse u Farenhajte

    # temp = 0

    # while temp != -1000:
    #     temp = eval(input("Unesite temperaturu za konverziju: "))
    #     if temp == -1000:
    #         print("Iskljucivanje programa...")
    #         break
    #     if temp < -273.15:
    #         print("Uneta temperatura je manja od apsolutne nule.")
    #         break
    #     print("Temperatura u farenhajtima iznosi: ", 9/5 * temp + 32)

# -Napisati program koji ispisuej Fibonacijev niz

    # prviBroj = 1
    # drugiBroj = 1

    # print(prviBroj)

    # for i in range(10):
    #     rezultat = prviBroj + drugiBroj
    #     prviBroj = drugiBroj
    #     drugiBroj = rezultat
    #     print(prviBroj)

# -Napisati program koji ispisuje slovo po slovo uneti string

# tekst = 'Ovo je uneti tekst'

# for i in tekst:
#     print(i, end=' ')

# -Napisati program koji proverava da li je uneti broj prost

# broj = eval(input("Unesite broj koji zelite da proverite da li je prost: "))
# prost = True
# from math import sqrt

# for i in range(2, round(sqrt(broj))):
#     if broj <= 0:
#         print("Uneli ste broj koji nije prirodan")
#         break
#     if broj == 1:
#         print("Uneti broj je prost")
#         break
#     if broj % i == 0:
#         print("Uneti broj nije prost")
#         prost = False
#         break

# if prost: 
#     print("Broj koji ste uneli je prost!")

#IMPORTI

# from math import pow
# from math import *
# from random import randint

# #NEGACIJA

# if not (10):
#     print('sth')

# #GRANANJE

# if 'uslov':
#     print()
# elif 'nekiNoviUslov':
#     print()
# else:
#     print()