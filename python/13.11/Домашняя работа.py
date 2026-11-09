"""Задание 1"""
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
summa = 0
negative_summa = 0
summa_nine = 0
for i in range(start, end):
    if i % 2 == 0:
        summa += i
    elif not i % 2 == 0:
        negative_summa += i
    elif i % 9 == 0:
        summa_nine += i
print("Сумма чётных чисел: ", summa) 
print("Сумма нечётных чисел: ", negative_summa)
print("Сумма чисел, кратных 9: ", summa_nine)

"""Задание 2"""
dlina = int(input("Введите длину линии: "))
sim = input("Введите символ: ")
for i in range(dlina + 1):
    print(sim)
    
"""Задание 3"""
while True:
    num = float(input("Введите число: "))
    if num == 7:
        print("Good bye!")
        break
    
    elif num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")
        
"""Задание 4"""
---