#Single line, Anonymous, Single expression


from functools import reduce


lambda x, y, z: x + y + z
lambda x,y : x * y
lambda : "Hello ........."

lam_example = lambda x, y, z: x + y + z
print(lam_example(1, 2, 3))

lam_example = 5
# print(lam_example(1, 2, 3))

#Where do we use lambda function
def add_3_num(x, y, z):
    return x + y + z


#Higher order functions - 

#map, reduce and filter

def double(x):
    return x * 2

def triple(x):
    return x * 3


print(list(map(lambda x: x * 5, [1, 4, 5, 6, 92, -32])))

print(list(map(double, [1, 3, 0.6, 12, -92, 32])))



def even(x):
    if x % 2 == 0:
        return True
    return False

print(list(filter(lambda x: x % 3 == 0, [1, 3, 6, 12, -92, 32])))


#Reduce - 
print(reduce(lambda x, y: x + y, [1, 3, 6, 12, -92, 32]))


#Scope: Global and Local scope

num1 = 25

def check():
    global num1

    num1 = 15
    globals()['num1'] = 45
    print(num1)

check()
print(num1)



#Naming conventions
#String immutability?



num1 = input()
num2 = input()
print(num1 + num2)


str1 = input()
str2 = input()
print(str1 + str2)


#Naming
#Name the variable properly - Give some context
#Variable names - case conventions
#Camel case, Pascal case, Snake case
#usernameConsoleInput
#UsernameConsoleInput
#username_console_input


username_console_input = input()

#Constants - We dont have constants in python

PIE = 3.14
DATABASE_PASSWORD = '12345'
PIE = 4.14