def classic():
  for i in range(5):
    for j in range(i+1):
      print('*',end=" ")
    print()
  
def multiply_method():
  p="* "
  for i in range(1,6):
    print(p*i)
  print()
  
def add_method():
  p="* "
  r=p
  for i in range(5):
    print(p)
    p+=r

def slice_method():
  p="* "
  p=p*5
  x=1
  for i in range(5):
    print(p[:x])
    x+=2

classic()
multiply_method()
add_method()
slice_method()
