# Задание 17

---

Для задания надо создать отдельную ветку от свежего мастера.
После решения задач, файлы и тесты закоммитить,
ветку запушить, создать в Гитхабе пулл-реквест.

УСЛОВИЕ: в своей домашней папке

Создать питоновский пакет с названием "lesson17"

В пакете создать модуль с именем соответствущего уровня

В модуле написать код согласно заданию уровня

ПРИМЕР:

```
homeworks/alexander_sidorov/lesson17/
    __init__.py     # пакет!
    level01.py      # вот!
    level02.py      # вот!
    test_lev1.py
    test_lvl02.py
```

```python
# homeworks/alexander_sidorov/lesson17/level01.py

def do(x, y):
    ...

class Doer:
    pass
```

---


## Уровень 1

Модуль: `level01`

Создать функцию с названием `key`.

Эта функция будет использоваться
в функции `sorted` как "ключевая":
будет управлять поведением сортировки.

Задача - написать такую логику внутри неё,
чтобы поведение `sorted` не изменилось.

Пример:

```python
def key(*a, **kw):
    ...

data = [3, 1, 2]

assert sorted(data) == sorted(data, key=key)
```

## Уровень 2

Модуль: `level02`

Создать функцию c названием `key`.

Эта функция будет использоваться
в функции `sorted` как "ключевая":
будет управлять поведением сортировки.

Задача - написать такую логику внутри неё,
чтобы поведение `sorted` не изменилось.

Пример:

```python
def key(*a, **kw):
    ...

data = [3, 1, 2]

assert sorted(data) == [2, 1, 3]  # но это не точно
``` 


## Уровень 3

Модуль: `level03`

Создать функцию c названием `my_map`.

Реализовать её логику таким образом,
чтобы она работала, как встроенная функция `map`,
только не была "ленивой": чтобы возвращала список.

Пример:

```python
assert list(map(f, k)) == my_map(f, k)
``` 


## Уровень 4

Модуль: `level04`

Создать функцию c названием `my_filter`.

Реализовать её логику таким образом,
чтобы она работала, как встроенная функция `filter`,
только не была "ленивой": чтобы возвращала список.

Пример:

```python
assert list(filter(p, k)) == my_filter(p, k)
``` 


## Уровень 5

Модуль: `level05`

Создать функцию c названием `trivial_decorator`.

Эта функция будет использоваться как декоратор.

Но логика будет предельно простая:
этот декоратор не должен никак изменять поведение
декорируемой функции.


## Уровень 6

Модуль: `level06`

Создать функцию c названием `benchmark`.

Эта функция будет использоваться как декоратор.

Логика будет такая:
запустить декорируемую функцию, вернуть результат,
предусмотреть случаи, что она может бросить ошибки...
и при всём этом нужно будет вывести - print-ами! - время её работы.

То есть, это время измерять и выводить будет декоратор.
Формат вывода времени — целое количество секунд.


## Уровень 7

Модуль: `level07`

Создать функцию c названием `typecheck`.

Эта функция будет использоваться как декоратор.

Логика будет такая.

Если в декорируемой функции присутствуют type hints,
те самые "подсказки" типов аргументов и возвращаемого результата,
то декоратор `typecheck` проверит, что при _запуске_
такой функции типы переданных значений в аргументах правильные,
совпадают с теми, что записаны в хинтах.

И аналогично, что функция вернула данные того
типа, который обещала.

Фактически, декоратор `typecheck` будет проводить
проверку типизации при исполнении функции.

Если какая-то проблема с типами, декоратор
должен бросать исключение `TypeError`


## Уровень 8

Модуль: `level08`

Создать класс c названием `Functor`.

Это будет класс, реализующий функционал функтора.

Суть такова: можно будет создать объект этого класса.

Ему в конструктор мы передадим:
1. функцию
2. аргументы для неё (но это не точно)
3. kw-аргументы для неё (но это не точно)

А потом, когда-нибудь, где-нибудь,
мы попытаемся этот объект, созданный объект класса `Functor`,
вызвать как функцию. Объект.

Чтобы он выполнился, да как: вызвал сохранённую
функцию с сохранёнными аргументами, и вернул её
результат.