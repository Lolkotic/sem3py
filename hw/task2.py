# 2) Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(**kwargs):
    return list(kwargs.values())

print(user_data(name=input('Введите имя: '),
                surname=input('Введите фамилию: '),
                birthday=input('Введите дату рождения: '),
                town_or_city=input('Введите город: '),
                email=input('Введите email: '),
                tel=input('Введите номер телефона: ')))

