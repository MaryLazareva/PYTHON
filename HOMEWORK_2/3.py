# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input())
i = 0
stroka_sum = ''

while num > 2**i:
    stroka = str(2**i)
    stroka_sum = stroka_sum + stroka + ' '
    i += 1

print(stroka_sum)
