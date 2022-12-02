# 3) Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a=int(input("Введите 1е число: ")), b=int(input("Введите 2е число: ")), c=int(input("Введите 3е число: "))):
    if a+b > a+c and a+b > b+c:
        return a+b
    if a+c > a+b and a+c > b+c:
        return a+c
    if b+c > a+c and b+c > a+b:
        return b+c
print(my_func())
