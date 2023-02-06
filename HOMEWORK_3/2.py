n = int(input("Input amount numbers in array: "))
list = [int(input()) for _ in range(n)]
number = int(input("Number: "))
list.append(number)
list.sort()
if number != max(list):
    index_number = list.index(number)
    if list[index_number] - list[index_number - 1] > list[index_number + 1] - list[index_number]:
        print(f"Neighbour of number {number} is {list[index_number + 1]}")
    elif list[index_number] - list[index_number - 1] == list[index_number + 1] - list[index_number]:
        print(f"Neighbour of number {number} is {min(list[index_number + 1], list[index_number - 1])}")
    else:
         print(f"Neighbour of number {number} is {list[index_number - 1]}")

else:
    print(f"Neighbour of number {number} is {list[len(list)-2]}")