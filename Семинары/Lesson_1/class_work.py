# print("Введите первую строку: ")
# a = int(input())
# b = int(input('Введите вторую строку: '))
# print(a, ' + ', b, ' = ', a+b)

# c = 5.59
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# n = int(input("Введите кол-во километров, которое Вы проезжаете за день: "))
# m = int(input("Введите общее расстояние: "))
# print((m+n-1)//n)

# countStudens1 = int(input("Введите кол-воучеников в 1м классе: "))
# countStudens2 = int(input("Введите кол-воучеников во 2м классе: "))
# countStudens3 = int(input("Введите кол-воучеников в 3м классе: "))
# part = (countStudens1//2 + countStudens1%2)+(countStudens2//2 + countStudens2%2)+(countStudens3//2 + countStudens3%2)
# print(part)

# i = int(input("В какой вагон Вы сели: "))
# j = int(input("Какой вагон указан: "))
# if i==j:
#   print("Невозможно узнать количество вагонов.")
# else:
#   print(f"Общее количество вагонов: {i+j-1}")

a = int(input("Введите год: "))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
  print("YES")
else:
  print("NO")