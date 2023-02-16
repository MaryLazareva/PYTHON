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

