# # string="vishalkumarsingh"
# # string=list(string)
# # string.sort()
# # print(string)
# # print(1^1)
# # print(0^1)
# # print(0^0)
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# print(bin(num1))
# print(bin(num2))
# # print(int(bin(num1))^int(bin(num2)))
# name="vishalkumar singh"
# name.removeprefix("vis")
# print(name)
# from unicodedata import decimal
# print(int("1111",2))

# print(decimal("1101"))
# List=[1,2,3,4,5]
# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         result=[]
#         for i in range(len(nums)-1):
#             number=nums[i]
#             binary=bin(number)
#             binary_num=binary[2:len(binary)]
#             for j in range(i+1,len(nums)):
#                 num=nums[j]
#                 binary1=bin(num)
#                 binary__num1=binary1[2:len(binary1)]
#                 xor=binary_num^binary__num1
#                 # result.append(int(int(binary_num)^int(binary__num1),2))

#         return result
# obj=Solution()
# print(obj.findMaximumXOR(List))
# num=10
# binary1=bin(num)
# binary__num1=binary1[2:len(binary1)]
# print(binary1)
# xor=1100^int(binary__num1)
# print(xor)
# print(1100^1111)
# print(1111^0101)

# print(int(str(int(bin(10)[2:6])^int(bin(15)[2:6])),2))
# name="singh"
# print(name[::-1])
# num=float(input('Enter the number: ')
# num=int(input("Enter the number:"))
# # if num==int(num):
# #     print("Ture")
# # else:
# #     print("False")
# new_num=num//2
# if new_num==num/2:
#     print("True")
# else:
#     print("False")

# Sum of two numbers without using any arithmetic operators.
# num1=int(input("Enter the first numebr: "))
# num2=int(input("Enter the second number: "))
# list1=[num1,num2]
# print(sum(list1))
# list1=[1,2,3,4,8]
# k=int(input("Enter the value of k: "))
# for i in range(len(list1)):
#     if list1[i]==k:
#         k=k*2
# print(k)
# n=int(input("Enter the value of n: "))
# m=int(input("Enter the value of m: "))
# for  i in range(m-1):
#     n=n//2
#     print(n)
# print(n)
# name="aaaabbbcccddd"
# # print(set(name))
# new_str=""
# i=0
# while i<len(name):
#     ele=name[i]
#     if ele not in new_str:
#         new_str+=ele
#         i+=1
#     else:
#         i+=1
# print(new_str

# name="vishalsingh"
# name=name.replace("i","")
# print(name)
# print(name[::-1])
# name="a a a"
# name="A man, a plan, a canal: Panama"
# new_str=""
# name=name.low
# for ele in name:
#     if ele.isalpha():
#         new_str+=ele
# print("new_str ="+new_str)

# print(name)
# name=name.replace(" ","")
# name=name.replace(",","")
# print(name)
# if name==name[::-1]:
#     print(name)
#     print("True")
# else:
#     print("False")

# :
#                 x.append(l)
#                 return 0

# name=input("enter the name: ")
# list1=list(name)
# for i in range(len(list1)):
#     new_list=list1
#     ele=new_list.pop(i)
#     if new_list==new_list[::-1]:
#         print("True")
#         break
#     new_list.append(1)
#     new_list.insert(i,ele)
#     new_list.remove(1)
# print(False)


# def max3(num1,num2,num3):
#     if num1>num2:
#         if num1>num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2>num3:
#             return num2
#         else:
#             return num3

# num1=int(input("Enter first numeber: "))
# num2=int(input("Enter second numebr: "))
# num3=int(input("Enter third number: "))
# print(max(num1,num2,num3))

# from mimetypes import guess_all_extensions


# def check(num):
#     for i in range(5):
#         choice = int(input("Enter your guess: "))
#         if choice == num:
#             return "Heartly Congratulations..."
#         else:
#             print("Wrong guess. Try again...")
#     return "Game Over."


# num = int(input("Enter a number: "))
# secret_num = num*2
# print(check(secret_num))

# 20.
word = input("Enter words separated by space: ")
word_list = list(word.strip().split())
print(word_list)

# 21.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

# 22.
a = int(input("Enter a integer value: "))
b = int(input("Enter a integer value: "))
if a < 0 or b < 0:
    print("Error, both a and b must be non-negative")
else:
    print("Please proceed.")

# # 23.
# num1=float(input("Enter first number: "))
# num2=float(input("Enter second number: "))
# num3=float(input("Enter third number: "))
# num_list=[num1,num2,num3]
