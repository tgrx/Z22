def my_filter(function, listing):
    return [i for i in listing if function(i)]
