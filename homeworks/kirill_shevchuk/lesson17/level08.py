class Functor:
    def __init__(self, function, ar=None, kw=None):
        self.function = function
        self.ar = ar or ()
        self.kw = kw or {}
    def __call__(self):
        return self.function(*self.ar, **self.kw)
