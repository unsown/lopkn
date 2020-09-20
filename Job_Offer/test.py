#  from IPython import embed; embed(colors="neutral")
from num import my_function

def get_random_numbers(n):
    from random import seed
    from random import random
    ret = []
    seed(1)
    i = 0
    while i < n:
        value = random()
        ret.append(value)
        i = i + 1
    return ret

def test(n):
    print("First test case:")
    a = [5000000, 4366346346, 12411, 2141, 32, 5, 32, 32523523, 35325, 352]
    ret = my_function(a)
    print(ret)

    print("\nReal world test case:")
    import time

    print("\nGenerating %d random numbers ..." % (n))
    start = time.time()
    b = get_random_numbers(n)
    duration = time.time() - start
    print("Random number is generated in %f seconds" % (duration))

    print("\nSorting %d random numbers ..." % (n))
    start = time.time()
    ret = my_function(b)
    duration = time.time() - start
    print("With current algorithm, the job is done in %f seconds" % (duration))
    print("Done")
    #  print(ret)

if __name__ == "__main__":
    n = 1000

    import sys
    if (sys.argv.__len__() > 1):
        n = int(sys.argv[1])

    test(n)
