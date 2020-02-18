class Functor:
    def __init__(self, function, arg=None, kwarg=None):
        self.function = function
        self.arg = arg or ()
        self.kwarg = kwarg or {}

    def __call__(self):
        return self.function(*self.arg, **self.kwarg)
