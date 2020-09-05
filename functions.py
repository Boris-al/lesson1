# Задание 1 по слайдам "Функции"

#1 Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, приводит их к строке и отдает объединенными через разделитель delimiter
def get_summ(one, two, delimiter='&'):
    out1 = str(one)
    out2 = str(two)
    output = out1 + delimiter + out2
    return output

#2 Вызовите функцию, передав в нее два аргумента "Learn" и "python", положите результат в переменную и выведите ее значение на экран
result = get_summ("Learn", "python")
print(result)

#3 Сделайте так, чтобы результирующая строка выводилась заглавными буквами
print(result.upper())

