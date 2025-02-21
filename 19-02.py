# num1 = int(input("Enter a number"))
# if num1 > 0:
#     print("Positive")
# elif num1 == 0:
#     print("Zero")
# else:
#     print("Negative number")


# if num1 % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# print("Even") if num1 % 2 == 0 else print("Odd")

# age = 17

# print("Is eligible") if age >= 18 else print("Not eligible")

# #3 discrete number
# num1 , num2 , num3 = 72, 13, -4

# print(num1) if (num1 > num3 and num1 > num2) else print(num2) if num2 > num3 else print(num3)


# day = int(input("Enter the number"))

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")

# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid input")



#Calculator

operation = input("Enter operation to perform").lower() #add, mul, div, sub
op1 = float(input("Enter first number"))
op2 = float(input("Enter second number"))

if operation == 'add' or operation == '+':
    # if operation in ['add', '+']
    print(op1 + op2)
#sub
elif operation == 'mul' or operation == '*':
    print(op1 * op2)
elif operation == 'div':
    if op2 == 0:
        print("Division by zero is not possible")
    else:
        print(op1/op2)
else:
    print("Invalid operation")



#first extension - add, Add, ADD, ADd, 
#second extension - +, -, *, /



#Write a program to classify a character entered by the user as a vowel, consonant, or neither.

user_input = input("Enter a single character").lower()

if len(user_input) != 1:
    print("Invalid")
else:
    if user_input in ['a', 'e', 'i', 'o', 'u']: # user_input in 'aeiou' (aei)
        print("Vowels")
    elif user_input.isalpha():
        print("Consonants")
    else:
        print("Special character")