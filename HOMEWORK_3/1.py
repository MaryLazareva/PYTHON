# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

n = int(input("Input amount numbers in array: "))
list = [int(input()) for _ in range(n)]
number = int(input("Number: "))
print(f"How many times we see a number {number} in the array: {list.count(number)}")