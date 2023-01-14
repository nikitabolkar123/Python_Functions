# The Python built-in filter() function extracts only particular elements from an iterable (like list, tuple, dictionary, etc.)
# It takes a function and an iterable as arguments and applies the function passed as an argument to each element of the iterable;
# once this process of filtering is completed,
# it returns an iterator as a result. An iterable is a Python object that can be iterated over.
#using lambda even or odd
a=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda a:a%2==0,a))
for i in even:

    print(i)
#the filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not
#common elements
def func(var):
    list = ['a', 'e', 'i', 'o', 'u']
    if (var in list):
        return True
    else:
        return False
sequence = ['a', 'b', 'b', 'c', 'd', 'e', 'o', 'h']

# using filter function
filtered = filter(func, sequence)

for a in filtered:
    print(a)
#check adults
ages = [6, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)

#using lambda function
ages = [10, 80, 17, 46, 21, 60, 7]
adults = list(filter(lambda age: age > 18, ages))
print(adults)

list1=[1,2,3,4,5,6,7,8,9]
num=list(map(lambda x:x*2,list1))
print(num)

# to check whether a number is divisible by 5 or not..
number = [10, 3, 192, 55, 20, 77 , 91]

# we r creating a function that will return True if the number is divisible by 5
def divisible(n):
    return True if n%5==0 else False

#here we r calling the filter function
divisible_by_5 = filter(divisible, number)

# to print the class of returned object
print(type(divisible_by_5))

# print the list of filtered numbers
print(list(divisible_by_5))

## created a list of dictionaries having items and their respective prices
food = [
   {"Item":"Burger", "Price":50},
   {"Item":"Pizza", "Price":350},
   {"Item":"cold coffee", "Price":200},
   {"Item":"Chocolate Shake", "Price":120}
   ]

# creating a budget function to check what all items cost less than 150
def budget(food):
   if food["Price"] < 150:
       return True
   else:
       return False

# passing budget function and food as the arguments to the filter function
budget_items = filter(budget, food)

# iterating the filtered_items object to get the item names
for i in budget_items:
   print(dict(i)["Item"])
