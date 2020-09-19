def my_function(a):

 b = []



 while a:
  maximum = a[0]
  for item in a:
      
      
    if item < maximum:
       
            maximum = item
    
  b.append(maximum)
  
  a.remove(maximum)

 print(b)

def get_7_million_random_num():
    return [5000000, 4366346346, 12411,2141, 32, 5, 32, 32523523,35325,352]
    
def test_my_function():
    a = [5000000, 4366346346, 12411,2141, 32, 5, 32, 32523523,35325,352]
    my_function(a)
    
    b = get_7_million_random_num()
    my_function(b)

test_my_function()
