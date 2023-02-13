def stepen(num1, num2):
    if num2 == 0:
        return 1
    elif num2 < 0:
        return stepen(num1, num2 + 1) * 1 / num1

    return num1 * stepen(num1, num2 - 1)


num = stepen(int(input('number: ')), int(input('degree: ')))
print(f'number is {num}')
