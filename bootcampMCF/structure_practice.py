# *
# * *
# * * *
# * * * *
# * * * * *

# n = eval(input('Unesite visinu figure: '))
# for i in range(1, n + 1):
#     print('* ' * i)

# * * * * *
#   * * * * 
#     * * *
#       * * 
#         *

# n = eval(input('Unesite visinu figure: '))
# for i in range(n):
#     print('  ' * i + '* ' * (n - i))

#     *
#    * *
#   * * *  
#  * * * *
# * * * * *

# n = eval(input('Unesite visinu figure: '))
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '* ' * i)

# n = 5
#     *
#    * *
#   * * *  
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n = eval(input('Unesite visinu figure: '))
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '* ' * i)
# for i in range(1, n):
#     print(' ' * i + '* ' * (n - i))

# n = 7
#       *
#      ***
#     *****  
#    *******
#   *********
#  ***********
# *************
#       *
#       *
#       *


# n = eval(input('Unesite visinu figure: '))
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '*' * (2 * i - 1))
# for i in range(n//2):
#     print(' ' * (n - 1) + '*') 

# n = 7
#       *
#      * *
#     *   *  
#    *     *
#   *       *
#  *         *
# *************

# 1)
# def createTriangle(n):
#     for i in range(1, n + 1):
#         if i == n:
#             print('*' * (2 * n - 1))
#             break
#         str = ' ' * (n - i)
#         for j in range(1, 2 * i):
#             if j == 1 or j == 2 * i - 1:
#                 str += '*'
#             else:
#                 str += ' '
#         print(str)

# 2)
# def printLine(star1, star2):
#     str = ''
#     for i in range(1, star2 + 1):
#         if i == star1 or i == star2:
#             str += '*'
#         else:
#             str += ' '    
#     print(str)

# def createTriangle(n):
#     for i in range(1, n + 1):
#         if i == n:
#             print('*' * (2 * n - 1))
#             break
#         printLine(n - i + 1, n + i - 1)



# n = eval(input('Unesite visinu figure: '))
# createTriangle(n)

# n = 7
#       *
#      * *
#     *   *
#    *     *
#   *       *
#  *         *
# *           *
#  *         *
#   *       *
#    *     *
#     *   *
#      * *
#       *

# def printLine(star1, star2):
#     str = ''
#     for i in range(1, star2 + 1):
#         if i == star1 or i == star2:
#             str += '*'
#         else:
#             str += ' '    
#     print(str)

# def createDiamond(n):
#     for i in range(1, n + 1):
#         printLine(n - i + 1, n + i - 1)
#     for j in range(n - 1, 0, -1):
#         printLine(n - j + 1, n + j - 1)



# n = eval(input('Unesite visinu figure: '))
# createDiamond(n)
