# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))
c = 0

for i in range(s):
    if c != 1: 
        for j in range(p):
            if c != 1:
                if i+j == s and i*j == p:
                    print(f"Загаданные числа: {i} и {j}")
                    c = 1

