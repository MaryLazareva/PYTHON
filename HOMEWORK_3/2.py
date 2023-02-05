n = int(input("Input amount numbers in array: "))
list = [int(input()) for _ in range(n)]
number = int(input("Number: "))
list.append(number)
list.sort()
if number != max(list):
    index_number = list.index(number)
    print(f"Neighbour of number {number} is {list[index_number + 1]}")
else:
    print(f"Neighbour of number {number} is {list[len(list)-2]}")