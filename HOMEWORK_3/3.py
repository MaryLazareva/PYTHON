scrabble = {"AEIOULNSTRАВЕИНОРСТ" : 1, "DGДКЛМПУ" : 2, "BCMPБГЁЬЯ" : 3, "FHVWYЙЫ" : 4, 
            "KЖЗХЦЧ" : 5, "JXШЭЮ" : 8, "QZФЩЪ" : 10} 
word = input("Input word: ").upper()
sum_of_points = 0
for w in word:
    for key, value in scrabble.items():
        if w in key:
            sum_of_points += value
            break
print(f"Number of points: {sum_of_points}")
            
    