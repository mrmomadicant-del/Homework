"""Задание 1"""
numbers = [1, 3, 6, 8, 5, 10, 20, 30, 7, 13, -6, -3, -1, -9, -20]

negative = 0
even = 0
odd = 0
#Вычисление сумм
for i in numbers:
    if i < 0:
        negative += i
    elif i % 2 == 0:
        even += i
    else:
        odd += i
print("Сумма негативных чисел: ", negative)
print("Сумма чётных чисел: ", even)
print("Сумма нечётных чисел: ", odd)
#4. Произведение элементов с индексами, кратными 3
index = 1
for i in range(len(numbers)):
    if i % 3 == 0:
        index *= numbers[i]
print("Произведение: ", index)
#5. ---
#6. ---
        
"""Задание 2"""
numbers2 = [2, 4, 3, 5, -9, -6, -4, 7, 9, 32, 20, 11, -11]

even2 = []
odd2 = []
negative2 = []
positive = []

for j in numbers2:
    if j % 2 == 0:
        even2.append(j)
    else:
        odd2.append(j)
    if j < 0:
        negative2.append(j)
    elif j > 0:
        positive.append(j)
 
print("Чётные числа: ", even2)
print("Нечётные числа: ", odd2)
print("Негативные числа: ", negative2)
print("Положительные числа: ", positive)