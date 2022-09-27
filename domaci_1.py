# - Napisati program koji iz unetog stringa izbacuje sve samoglasnike.

    # str = 'Ja volim python'
    # noviStr = ''

    # for char in str:
    #     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    #         continue
    #     noviStr += char

    # print(noviStr)

# - Napisati program koji umece drugi string na polovinu prvog.

    # str_1 = 'Python'
    # str_2 = 'Avion'
    # refactored = str_1[:round(len(str_1)/2)] + str_2 + str_1[round(len(str_1)/2):]

    # print(refactored)

# - Napisati program koji proverava da li se karakteri iz drugog stringa nalaze u prvom.

# str_1 = 'Anak'
# str_2 = 'Ananas'
# postoji = False
# vazeciStr = False

# for char in str_1:
#     postoji = False
#     for c in str_2:
#         if c == char:
#             postoji = True
#     if postoji: 
#         vazeciStr = True
#     if not postoji:
#         print('Netacno')
#         vazeciStr = False
#         break

# if vazeciStr:
#     print('Svi karakteri iz prvog stringa postoje u drugom.')

# - Napraviti program koji uneti string ispisuje unatrag. Program se prekida kada se unese palindrom.

# while True:
#     str = input('Unesite string: ')
#     strZaIspis = str[::-1]
#     print(strZaIspis)
#     if str == strZaIspis:
#         print("Exiting...")
#         break
