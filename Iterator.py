#1st
mySecret = ["I", "Like", "Python"]

myIter = iter(mySecret)
print(myIter)

print(next(myIter))
print(next(myIter))
print(next(myIter))

print('---------------------------------------------------')
nums = [7,8,8,5]
it = iter(nums)
print(it.__next__())
print(next(it))
for i in nums:
    print(i)
#The next() function returns the next item in an iterator.
# You can add a default return value, to return if the iterable has reached to its end.

def table(n):
    for i in range(1, 9):
        yield n * i


for i in table(12):
    print(i)

print('---------------------------------------------------')
my_string = ("nikita", "nita", "geeta")
my_it = iter(my_string)

print(next(my_it))
print(next(my_it))
print(next(my_it))

mystr= "pratiksha"
my_it = iter(mystr)

print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))

print('---------------------------------------------------')
class TopTen:
    def __init___(self):
        self.num = 1

    def __init__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise stopIteration


values = TopTen()
print(next(values))
for i in values:
    print(i)
