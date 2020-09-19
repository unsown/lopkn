#  from IPython import embed; embed(colors="neutral")
from num import my_function

def get_7_million_random_num():
    return [5000000, 4366346346, 12411, 2141, 32, 5, 32, 32523523, 35325, 352]

def test_my_function():
    a = [5000000, 4366346346, 12411, 2141, 32, 5, 32, 32523523, 35325, 352]
    ret = my_function(a)
    print(ret)

    b = get_7_million_random_num()
    ret = my_function(b)
    print(ret)

test_my_function()
