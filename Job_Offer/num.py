def my_function(a):
    b = []
    while a:
        maximum = a[0]
        for item in a:
            if item < maximum:
                maximum = item
        b.append(maximum)
        a.remove(maximum)
    return(b)
