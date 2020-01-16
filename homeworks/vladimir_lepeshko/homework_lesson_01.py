""" Select programs"""

import platform
import datetime


# Домашнее задание

# Задание 1: написать программу, которая выводит "Hello, World!".


def hello_world():
    """ Hello World! only"""
    greeting = "Hello, World!"
    print(greeting)


# Задание 2: написать программу, которая выводит информацию о вас.


def date_of_birth():
    """ ID information"""
    name = input("Введите Ваше ФИО: ",)
    date = datetime.date(1988, 10, 5)
    mood = input("Ваше настроение сегодня: ",)
    print(("ФИО: " + name, "Дата рождения: " + str(date), "Настроение: " + mood))


# Задание 3: вывести информацию о системе, на которой запущена программа.


def os_version():
    """ Platform version"""
    return print(platform.uname())


# Задание 4: программа, которая спрашивает имя пользователя и приветствует его


def greet_id():
    """ Greeting ID"""
    ask_name_id = str(input("Как Вас зовут? "))
    print(str("Доброго времени суток, " + ask_name_id + "! Начнем работу!)"))


# Задание 5: предоставить выбор одного из вариантов программ

FUNCTIONS = {
    "1": hello_world,
    "2": greet_id,
    "3": date_of_birth,
    "4": os_version,
}


CHOICE = input("Введите число от 1 до 4 для выбора программы: ")
PERFOMANCE = FUNCTIONS[CHOICE]
PERFOMANCE()
