#Задача 4
#Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
counter = 0
proiz = 1
print('Ряд: ')
while counter < 10:
    counter += 1
    print(counter)
    proiz *= counter
print('Произведение ряда:', proiz)