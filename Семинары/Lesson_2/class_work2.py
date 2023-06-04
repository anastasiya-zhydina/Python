# Task_1
# По данному целому неотрицательному n вычислите значение n! = 1*2*3*...*N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
"""
n = int(input("Введите число: "))
i = 2
result = 1
while i <= n:
    result *= i
    i += 1
print(f"{n}! = {result}")
"""

#Task_2
# Дано натуральное число A>1.
# Определите, каким по счету числом Фибоначчи оно является, т.е. введите такое число
# n, что Ф(n) = A.
# Если А не является числом Фибоначчи, введите число -1.

"""
n = int(input("Введите число: "))
n0 = 0 #посути n0 - это последующее число Фибоначчи, т.е. третье число
a0 = 0
a1 = 1
i = 2 # равно 2, потому что уже знаем первые два числа
while n0<n:
    n0 = a0 +a1
    a0 = a1
    a1 = n0
    i += 1
    if n0>n: #если встретилось это значение, то данное число не может являться числом Фибоначчи
        i=0
if i != 0:
    print(i)
else: 
    print(-1)
"""
#метод флажка, что это???? замена функции break
"""
n = int(input("Введите число: "))
flag = True
while flag:
    if n == 100:
        flag = False
    n += 1
print(n)
"""

#Task_3 (на цикл for)
# Синоптиков интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют
# период, в который среднесуточная температура ежедневно превышала 0 градусов по Цельсию.
# Написать программу, помогающую синоптикам в работе.
# Пользователь вводит число N - общее количество рассматриваемых дней (1<=N<=100).
# В следующих строках располагается N целых чисел.
# Каждое число - среднесуточная температура в соответсвующий день.
# Температуры - целые числа и лежат в диапазоне от -50 до 50.

"""
n = int(input("Введите кол-во дней: "))
max_day_positive = 0       #кол-во дней с +температурой
count = 0                  #количественная переменная, которая считает количество дней с t>0
for i in range(n):         #запускаем цикл for на то кол-во раз, сколько ввелпользователь
    x = int(input("Введите температуру дня: ")) #каждый раз вводим новое значение t
    if x >0:               #если х > 0 то count увеличиваем
        count += 1
    else:                  # иначе обнуляем count
        count = 0
    
    if max_day_positive < count:
        max_day_positive = count  
print(max_day_positive)
"""
#Task_4
# Необходимо выбрать два арбуза с минимальной массой и максимальной.
# Пользователь вводит число N - кол-во арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число - 
# это масса соответсвующего арбуза
# нахождение min и max 

n = int(input("Введите кол-во арбузов: "))
max_massa = 0
min_massa = 1000 
for i in range(n):
    x = int(input("Введите массу арбуза: "))
    if x > max_massa:
        max_massa = x
    elif x < min_massa:
        min_massa =x
print(min_massa, max_massa)

        
