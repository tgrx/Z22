def my_filter(func, collection):
    return [elm for elm in collection if func(elm)]
