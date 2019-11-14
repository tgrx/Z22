# Ответы на вопросы

## Какую литературу почитать?

- [Документация](https://docs.python.org/3/index.html)
- [Вики](https://wiki.python.org/moin/)
- Книги ([тысячи их](https://realpython.com/best-python-books/), но многие начинают с Лутца)

Так же документацию можно читать на лету.

Для этого:

1. запускаем python: `python`
    
    Откроется интерпретатор, в интерактивном режиме.
    Будет видно приглажение печатать: `>>>`;
    
1. Берём какую-нибудь сущность

    Например: `print`, `locals`.
    Или какой-нибудь модуль из библиотеки, например `os` - только сначала его надо импортировать: `import os`;

1. И передаём его в функцию `help`:

    ```python
    >>> help(print)
    
    >>> help(locals)
    
    >>> import os; help(os)
   
    # даже так!
    >>> help(help)
    ``` 
   
   НО! нужно умение читать по-английски.

## Как работать с Git в Windows?

Можно в терминале. Если Git установлен правильно,
то он как команда "git" будет доступен
и в стандартном терминале (Пуск-Выполнить-cmd),
и в терминале от Git SCM.

Кроме этого, установленный Git интегрируется в PyCharm.

Кроме этого, есть графические клиенты, [вот список](https://git-scm.com/download/gui/windows#).

## Какие есть IDE?

Существует огромное количество списков ТОП-10 и обзоов на [IDE](https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F_%D1%81%D1%80%D0%B5%D0%B4%D0%B0_%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8), вот, например: [https://www.programiz.com/python-programming/ide](https://www.programiz.com/python-programming/ide)

Рекомендую:

- [PyCharm](https://www.jetbrains.com/pycharm/)
- [VSCode](https://code.visualstudio.com/)

Отдельно стоит посмотреть на [Jupyter](https://jupyter.org/)
