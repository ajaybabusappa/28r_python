# # n = int(input("Enter the number"))

# # sum = 0
# # for i in range(1, n + 1):
# #     print(i)
# #     sum += i
    
# # print(sum)

# # #Time complexity - 
# # print((n*(n+1))/2)




# # for i in range(0, n): #O(N * M) => O(N square)
# #     for j in range(1, m):
# #         print(i, j)
        
        
        
# # list1 = [1,2, 3, 4, 5, 6, 7, 7, 7, 7]
# # duplicates = []
# # for i in list1:
# #     if i not in duplicates:
# #         duplicates.append(i)
        
        
# #O(1) < O(logn) < O(n) <O(nlogn) <O(n square)


# #Space complexity - O(1) < 






# #Reverse a number - 12573 - 37521
# #Rem - 1257, 3
# #125, 7
# #12, 5
# #1, 2
# #0, 1
# num1 = 12473

# dig_sum = 0
# rev_num = 0
# while num1 > 0:
#     rem = num1 % 10
#     dig_sum += rem
#     rev_num = rev_num * 10 + rem #3#37#374#3742#37421
#     num1 = num1 // 10 #1247 #124#12#1#0
    
# print(dig_sum)
# print(rev_num)    



# while True:
#     num1 = int(input("Enter a non negative number"))
#     if num1 < 0:
#         break



num1 = 1
while num1 >= 0:
    num1 = int(input("Enter a non negative number "))




db_username = 'Dj Tillu'
db_password = 'Radhika'

total_chances = 3

while total_chances > 0:
    input_username = input("Enter username")
    input_password = input("Enter password")

    if input_username == db_username and input_password == db_password:
        print("Logic succesful")
        break
    else:
        total_chances -= 1
        print("You still have", total_chances, "chances")


