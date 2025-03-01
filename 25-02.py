# #Prime number - 1 and itself
# #4 variations

# num1 = int(input("Enter a num to check for prime"))

# #25
# # count = 0
# # for i in range(1, num1 + 1):
# #     if num1 % i == 0:
# #         count += 1

# # print("Prime") if count == 2 else print("Composite")


# #4 - 2, 3
# #25 

# if num1 in [0, 1] or num1 < 0:
#     print("Invalid")
# else:
#     spy = True
#     for i in range(2, num1):
#         print("Loop entered")
#         if num1 % i == 0:
#             spy = False
#             print("Not a prime")
#             break

#     if spy:
#         print("Prime")


# #16 -> 1, 2, 4, 8, 16
# #22 -> 1, 2, 11, 22
# # 6 -> 1, 2, 3, 6



# #Approach 3
# if num1 in [0, 1] or num1 < 0:
#     print("Invalid")
# else:
#     spy = True
#     for i in range(2, (num1 // 2) + 1):
#         print("Loop entered")
#         if num1 % i == 0:
#             spy = False
#             print("Not a prime")
#             break

#     if spy:
#         print("Prime")


# #Approach 4
# #64
# #1 * 64 = 64
# #2 * 32
# #4 * 16
# #8 * 8
# #16 * 4
# #32 * 2
# #64 * 1


# #Approach 3
# if num1 in [0, 1] or num1 < 0:
#     print("Invalid")
# else:
#     spy = True
#     for i in range(2, int(num1 ** 0.5) + 1):
#         print("Loop entered")
#         if num1 % i == 0:
#             spy = False
#             print("Not a prime")
#             break

#     if spy:
#         print("Prime")




#Assginment 1 - Print primes in a range


#Fib - f(n) = f(n-1) + f(n-2) i.e n = 0 value 0
#n = 1
# 0 1 1 2 3 5 ...

n = 15
num1 = 0
num2 = 1

print(num1)
print(num2)


for i in range(1, n-1):
    temp = num1 + num2
    print(temp)
    num1 = num2
    num2 = temp





#1, 2, 3,......N
budget = 0
for i in range(1, 40):
    if i % 2 == 0:
        team_budget = i * 100
        budget += team_budget 
print(budget)


#perfect number
num1 = int(input("Enter the number"))
#6 - 1, 2, 3, 6
sum = 0
for i in range(1, num1):
    if num1 % i == 0:
        sum += i

if sum == num1:
    print("Perfect number")
else:
    print("Not a perfect number")



num2 = 12473
num1 = num2

rev_num = 0
while num1 > 0:
    rem = num1 % 10
    rev_num = rev_num * 10 + rem #3#37#374#3742#37421
    num1 = num1 // 10 #1247 #124#12#1#0

if rev_num == num2:
    print("Palindrome")
else:
    print("Not a palindrome")
