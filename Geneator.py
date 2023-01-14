# A generator is a special type of function which does not return a single value,
# instead, it returns an iterator object with a sequence of values.
# sequence of element
#1st Example
def display(a, b):
    # yield statement returns the statement from the generator function into the generator objects
    yield a
    yield b


x, y = display(10, 20)
print(x)
print(y)


# 2nd example
def show(a, b):
    while a <= b:
        yield a
        a += 1


x = show(1, 5)
print(type(x))
print(next(x))  # next function used to retrieve element from the generator  object
print(next(x))
print(next(x))
print(next(x))
print(next(x))


def gen_fun():
    yield 10
    yield 20
    yield 30


for x in gen_fun():
    print(x)

print('------------------------------------------------------')
#3rd example
def table(n):
    for x in range(1, 11):
        yield n * x
        x = x + 1

for x in table(15):
    print(x)

print('------------------------------------------------------')
def my_generator(n):

    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # it will increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(6):

    print(value)

print('------------------------------------------------------')

def infinite():
    n = 0
    while True:
        yield n
        n += 1


for i in infinite():
    if i % 4 == 0:
        continue
    elif i == 13:
        break
    else:
        print(i)

print('------------------------------------------------------')

def multiple_yield():
    str1 = "Nikita"
    yield str1

    str2 = "Priyanka"
    yield str2

    str3 = "Saurav"
    yield str3


obj = multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))