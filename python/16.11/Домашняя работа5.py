import random
list1 = [random.randint(1, 20) for i in range(10)]
list2 = [random.randint(1, 20) for j in range(10)]

"""Задача 1"""
list3 = list1 + list2
print("Оба списка в одном", list3)

"""Задача 2"""
list4 = []
for number in list1 + list2:
    if number not in list4:
        list4.append(number)
print("без повторений", list4)

"""Задача 3"""
list5 = []
for numberr in list1:
    if numberr in list2 and numberr not in list5:
        list5.append(numberr)
print("Общие цифры", list5)

"""Задача 5"""
list6 = [min(list1), max(list1), min(list2), max(list2)]
print("Минимальные и максимальные значения", list6)