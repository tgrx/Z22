# Задание 05

---

Для задания надо создать отдельную ветку от свежего мастера.
После решения задач, файлы и тесты закоммитить,
ветку запушить, создать в Гитхабе пулл-реквест.

УСЛОВИЕ: в своей домашней папке

Создать питоновский пакет с названием "hw05"

В пакете создать модуль с именем соответствущего уровня

В модуле создать функцию с названием согласно заданию уровня

ПРИМЕР:

```
homeworks/alexander_sidorov/hw05/
    __init__.py     # пакет!
    level01.py      # вот!
    level02.py      # вот!
    test_lev1.py
    test_lvl02.py
```

```python
# homeworks/alexander_sidorov/hw05/level01.py

def summa(x, y):
    return x + y
```

---


## Уровень 1

Модуль: `level01`

Создать функцию c названием `summa`,
которая принимает 2 позиционных аргумента
и возвращает их сумму.

```python
assert summa("1", "2") == "12"
```


## Уровень 2

Модуль: `level02`

Создать функцию c названием `hello`,
которая принимает 1 позиционный аргумент: имя
и возвращает строку "Hello, {имя}!".

```python
assert hello("Alex") == "Hello, Alex!"
```


## Уровень 3

Модуль: `level03`

Создать функцию c названием `good_phone`,
которая принимает 1 позиционный аргумент: телефон
и сообщает, правильный ли это номер.

```python
assert good_phone("+375172294660")
assert good_phone("+375296648778")
assert not good_phone("+791562655123")
assert not good_phone("2020327")
```


## Уровень 4

Модуль: `level04`

Создать функцию c названием `host`,
которая принимает 1 позиционный аргумент: URL
и возвращает имя хоста. Если URL неправильный
и хост вычислить невозможно — возвращает пустую строку.

```python
assert host("test.com/a/b/c") == "test.com"
assert not host("/a/b")
assert host("/a/b") == ""

assert host("https://github.com/tgrx/Z22/") == "github.com"
assert host("git@github.com:tgrx/Z22.git") == "github.com"
```


## Уровень 5

Модуль: `level05`

Создать функцию c названием `unique`,
которая принимает 1 позиционный аргумент — некую коллекцию —
и сообщает,
содержит ли эта коллекция
повторяющиеся элементы,
или нет.

```python
assert unique("123")
assert not unique((1, 1))
```


## Уровень 6

Модуль: `level06`

Создать пару функций с названиями `enqueue` и `dequeue`,
которые будут эмулировать работу со списком как с очередью [FIFO](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics). 

Функция `enqueue` принимает два позиционных аргумента:
первый — сама очередь: список, второй — элемент, любого типа.
Функция добавляет элемент в конец очереди.
Функция ничего не возвращает.

Функция `dequeue` принимает один позиционный аргумент: саму очередь, список.
Функция достаёт элемент из очереди и возвращает его.
Если очередь пустая — возвращает `None`.

```python
q = []

assert enqueue(q, 100) is None
assert enqueue(q, 200) is None
assert len(q) == 2

assert dequeue(q) == 100
assert len(q) == 1

assert enqueue(q, 300) is None
assert len(q) == 2

assert dequeue(q) == 200
assert dequeue(q) == 300
assert len(q) == 0

assert dequeue(q) is None
assert len(q) == 0
```


## Уровень 7

Создайте пару функций,
которые бы работали со словарём (`dict`)
как с очередью с приоритетами:

```python
def enqueue(l, p, e):
    """ добавляет элемент e в конец очереди l с приоритетом p """

def dequeue(l):
    """
    вынимает элемент из начала очереди и возвращает его
    если очередь пуста - возвращается None
    элементы возвращаются согласно приоритету
    """
```

Пример:

```python
x = {}
assert dequeue(x) is None
assert enqueue(x, 1, "a") is None
assert enqueue(x, 1, "b") is None
assert enqueue(x, 2, "aa") is None
assert dequeue(x) == "aa"
assert enqueue(x, 1, "c") is None
assert enqueue(x, 3, "aaa") is None
assert enqueue(x, 3, "bbb") is None
assert enqueue(x, 2, "bb") is None
assert dequeue(x) == "aaa"
assert dequeue(x) == "bbb"
assert dequeue(x) == "bb"
assert dequeue(x) == "a"
assert dequeue(x) == "b"
assert dequeue(x) == "c"
assert dequeue(x) is None
assert x == {}
```
