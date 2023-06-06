# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

count_first = int(input("Введите количество элементов в первом множесте: "))
count_second = int(input("Введите количество элементов во втором множестве: "))
set_first = set()
set_second = set()
while count_first > 0:
    input_value = input("Введите элемент: ")
    set_first.add(input_value)
    count_first = count_first - 1
while count_second > 0:
    input_value = input("Введите элемент: ")
    set_second.add(input_value)
    count_second = count_second - 1
result = set_first & set_second
result = list(result)
result.sort()
print(result)