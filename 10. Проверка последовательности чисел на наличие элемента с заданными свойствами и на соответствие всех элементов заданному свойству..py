# Проверка последовательности чисел на наличие элемента с заданными свойствами

N = int(input())  # Количество элементов последовательности
index = -1  # Порядковый номер элемента с заданными свойствами

for i in range(N):
    element = int(input())
    if element == 1:  # заданное условие
        index = i
if index == -1:
    print("False")  # В последовательности нет элементов с заданными свойствами
else:
    print("True")  # В последовательности есть хотя бы один элемент с заданными свойствами

# Проверка последовательности на соответствие всех элементов заданному свойству

N = int(input())  # Количество элементов последовательности
indicator = 0  # Количество элементов последовательности, удовлетворяющих заданному свойству
for i in range(N):
    element = int(input())
    if element == 1:  # заданное свойство
        indicator += 1
if indicator == N:
    print("True")  # Все элементы последовательности удовлетворяют заданному свойству
else:
    print("False")  # Не все элементы последовательности удовлетворяют заданному свойству
