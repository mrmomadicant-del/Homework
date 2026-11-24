"""Задача 1"""
try:
    number = int(input("Введите целое число: "))
    print(number ** 2)
except ValueError:
    print("Это не целое число")
    
"""Задача 2"""
try: 
    number1 = int(input("Введите первое целое число: "))
    number2 = int(input("Введите второе целое число: "))
    print(number1 / number2)
except ValueError:
    print("Это не целое число")
except ZeroDivisionError:
    print("На 0 делить нельзя")
    
"""Задача 3"""
try:
    week = int(input("Выберите день недели от 1 до 7: "))
    if week == 1:
        print("Понедельник")
    elif week == 2:
        print("Вторник")
    elif week == 3:
        print("Среда")
    elif week == 4:
        print("Четверг")
    elif week == 5:
        print("Пятница")
    elif week == 6:
        print("Суббота")
    elif week == 7:
        print("Воскресенье")
    else:
        raise IndexError
except IndexError:
    print("Нет такого дня")
except ValueError:
    print("Выберите цифрой")
finally:
    print("Проверка завершена")





    