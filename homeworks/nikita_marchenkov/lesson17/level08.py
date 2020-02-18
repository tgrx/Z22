class Functor:
    def __init__(self, func, args=None, kwargs=None):
        self.func = func
        self.args = args or ()
        self.kwargs = kwargs or {}

    def __call__(self, *args, **kwargs):
        return self.func(*self.args, **self.kwargs)
