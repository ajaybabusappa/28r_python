# #Functions - What are functions?

# #def example_function()
# #Loops vs functions

# def example_function():
#     print("Statement 1")
#     print("Statement 2")
#     print("Statement 8")
#     print("Statement 4")
#     print("Statement 5")


# print("I'm doing some operations")

# example_function()

# print("I'm doing some other operations")

# example_function()

# example_function()


# example_function()


#r is a parameter
def calc_volume(r, pie = 3.14):
    print(r)
    print(pie)
    print(4/3 * pie * r ** 3)


#Positional arguments
calc_volume(10, 3.14)
calc_volume(20, 3.14)
calc_volume(8)


#keyword arguments
calc_volume(pie = 3.14, r = 25)
# calc_volume(pie = 4.15, 10)
calc_volume(10, pie = 4.15)

#Default arguments
#Positional arguments follows default arguments
#Non default arguments follows default argument error


def calc(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    return a + b, a-b, a* b, a/b
    print("Hi Bro")


res1 = calc(2, 5)
print(res1)


num1 = 10

def even_or_odd(num1):
    if num1 % 2 == 0:
        return "Even"
    return "Odd"


#arbitrary arguments and keyword arguments
# def sum(a, b):
#     return a + b


# def sum(a, b, c):
#     return a + b + c

# def sum(a, b, c , d):
#     return a + b + c + d


# sum(2, 3)


def sum (a, *args):
    print(a)
    print(args)
    res  = a
    for i in args:
        res += i

    print(res)
    return res


sum(3, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13)


#

def sum1 (**kargs):
    print(type(kargs))
    res = 0
    for key, value in kargs.items():
        res += value
    print(res)
    return res
sum1 (num1 = 3, num2 = 4, num3 = 5)
