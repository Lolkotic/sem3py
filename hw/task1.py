# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
#
def task1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Делить на ноль нельзя')


print(task1(int(input('Введите делимое: ')), int(input('Введите делитель: '))))






