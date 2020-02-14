class Functor:
    def __init__(self, function, args, kwargs):
        self.__function = function
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self):
        return self.__function(*self.__args, **self.__kwargs)
