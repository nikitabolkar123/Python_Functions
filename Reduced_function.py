#The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of
#the list elements mentioned in the sequence passed along
#reduced Function
from functools import reduce
val=[1,2,3,4,5]
add=reduce(lambda a,b:a+b,val)
print('Addition=',add)

#Factorial Number
import functools
def prod(x,y):
    print("x=",x," y=",y)
    return x*y
fact=functools.reduce(prod, range(1, 5))
print ('Factorial of 4: ', fact)

#maximum numbera
from functools import reduce
def myfunc(a,b):
    if a > b:
        return a
    else:
        return b
val = [1,2,3,4,5]
max=reduce(myfunc,val)
print('max=',max)

#maximum number using Lambda
from functools import reduce
value=[1,2,3,4,5]
maximum= reduce(lambda a,b:a if a>b else b,value)
print('maximum value=',maximum)
