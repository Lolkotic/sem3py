# 5) Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_of_nums(*nums):
    sum = 0
    smth_else = False
    for num in nums:
        try:
            if num:
                sum += int(num)
        except ValueError:
            smth_else = True
    return sum, smth_else

sum_of_all_nums = 0

while True:
    numbers_from_user = input('Введите числа через пробел: ').split(' ')
    sum, smth_else_stop = sum_of_nums(*numbers_from_user)
    sum_of_all_nums += sum
    print(f'сумма Ваших чисел =  {sum_of_all_nums}')

    if smth_else_stop:
        break



