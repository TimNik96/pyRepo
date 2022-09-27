# -Napisati program koji proverava da li je uneta sifra tacna. Za sve dogadjaje ispisati adekvatne poruke korisniku.

    # sifra = "pythonKurs"
    # unetaSifra = input("Unesite sifru: ")

    # while sifra != unetaSifra:
    #     print("Sifra koju ste uneli je netacna.")
    #     unetaSifra = input("Unesite sifru: ")

    # print("Dobrodosli!")

# -Napisati program koji omogucava korisniku da pogodi broj koji je zamislio racunar u rasponu od 1 do 10. (ispisati koliko puta je pokusano, kao i koji je broj zamisljen)

# from random import randint

# zamisljeniBroj = randint(1, 10)
# brojPokusaja = 0
# brojIzUnosa = eval(input("Pogodite broj: "))

# while zamisljeniBroj != brojIzUnosa:
#     print("Pogresan broj!")
#     brojPokusaja += 1
#     brojIzUnosa = eval(input("Pogodite broj: "))

# print("Trazeni broj je", zamisljeniBroj, "a pogodili ste ga iz", brojPokusaja, "puta.")

# -Napisati program koji iscrtava trougao za unetu visinu.

# n = eval(input("Uneti visinu trougla: "))

# for i in range(1, n+1):
#     print("*" * i)
