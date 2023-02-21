def words(sentense, letters):
    array = []
    for i in range(len(sentense)):
        count = 0
        for word in sentense[i]:
            for letter in word:
                if letter in letters:
                    count += 1
        array.append(count)
        
    if len(set(array)) == 1:
        return "Парам пам-пам"
    return "Пам пара"
            
sentense = [r.split('-') for r in input().split()]
letters = ['о', 'а', 'и', 'е', 'ё', 'ы', 'э', 'ю', 'я', 'у']
print(words(sentense, letters))

# alp = "аеёиоуыэюя"
# word_sug = input().split()
# vowel_letters = [sum([True for j in word if j.lower() in alp]) for word in word_sug]

# if all(vowel_letters) and len(set(vowel_letters)) == 1:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

# 2 вариант

# def vowels_counter(S):
#     vowels = list('а е ё и о у ы э ю я'.split())
#     vowels_counter = list()
#     for i in S:
#         counter = 0
#         for ch in i:
#             if ch in vowels:
#                 counter += 1
#         vowels_counter.append(counter)
#     return vowels_counter

# # пара-ра-рам рам-пам-папам па-ра-па-дам
# s = list("ff ff ff".split())  # можно заменить на input().split()

# print("Парам пам-пам" if len(set(r := vowels_counter(s))) == 1 and r[0] != 0 else "Пам парам")