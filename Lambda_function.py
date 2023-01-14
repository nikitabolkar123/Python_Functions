#add number
add=lambda a: a+10
print(add(5))

#multiplication number
mul=lambda a,b: a*b
print(mul(10,20))

#cube of number
cube=lambda a:a*a*a
print(cube(3))

# lambda that accepts one argument
name_user = lambda name : print('here is', name)
# lambda call
name_user('nikita')

#maximum  number
max = lambda a, b: a if (a > b) else b
print(max(15, 7))

#program to count the even, odd numbers in a given array of integers using Lambda.
array_no = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(array_no)
#the filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not
even_count = len(list(filter(lambda no: (no%2 == 0) , array_no)))
odd_count = len(list(filter(lambda no: (no%2 != 0) , array_no)))
sqr_list = list(map( lambda no: no ** 2 , array_no ))
#map() used to apply a function all the elements in a sequence
print("Number of even count is", even_count)
print("Number of odd count is: ", odd_count)
print("Square of the list items are:",sqr_list )


# all the  elements of a list to upper case using lambda and map() function
names = ['nikita', 'rajshri', 'komal', 'raj']
# we have to change all name in upper case and return the same
uppered_names = list(map(lambda names: names.upper(), names))
print(uppered_names)

#check age
ages = [10, 80, 17, 46, 21, 60, 7]
adults = list(filter(lambda age: age > 18, ages))
print(adults)

## check if two numbers is equal or greater or lesser
number= lambda a, b: f"{a} is smaller than {b}" \
    if a < b else (f"{a} is greater than {b}" if a > b \
                       else f"{a} is equal to {b}")
print(number(15, 14))
print(number(10, 10))
print(number(10, 13))

#product of number
product = lambda x,y,z:x*y*z
print(product(z=10,x=20,y=40))

#string present or not
sub_string =lambda string : string in "Python is case sensitive"
print(sub_string('Python'))

#multiply number by 2
list1=[1,2,3,4,5,6,7,8,9]
num=list(map(lambda x:x*2,list1))
print(num)