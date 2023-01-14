#no multiply by two
#map() used to apply a function all the elements in a sequence
list1=[1,2,3,4,5,6,7,8,9]
num=list(map(lambda x:x*2,list1))

#2nd no increase by two
a=[1,3,7,9,8,5]
def inc(n):
    return n+2
result = map(inc,a)
print(result)
for i in result:
    print(i)

#addition of list
num1 = [2, 5, 8]
num2 = [4, 5, 6]

res = map(lambda x, y: x + y, num1, num2)
print(list(res))


#square of the number
def square(num):
    return num*num
my_list = [2,3,4,5,6,7,8,9]
new_list = map(square, my_list)
print(new_list)
print(list(new_list))

#uppecase letter
def mymapfunc(x):
    return x.upper()
my_str = "here is nikita!"
updated_list = map(mymapfunc, my_str)
print(updated_list)
for i in updated_list:
    print(i, end="")

#Passing one Tuple and a list iterator to map()
def myfunc(list1, tuple1):
    return list1+"_"+tuple1
my_list1 = ['a','b', 'b', 'd', 'e']
my_tuple = ('C#','Java','Python','C++','C')

new_list1 = map(myfunc, my_list1,my_tuple)
print(new_list1)
print(list(new_list1))