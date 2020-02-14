class Functor:
    def __init__(self, function, ar, kw):
        self.function = function
        self.ar = ar
        self.kw = kw
    def __call__(self):
        return self.function(*self.ar, **self.kw)
