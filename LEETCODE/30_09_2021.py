# list1=[9,4,3,2]
# result=0
# for i in range(len(list1)-1):
#     k=i+1
#     for j in range(k,len(list1)):
#         if list1[i]<list1[j]:
#             if result<list1[j]-list1[i]:
#                 result=list1[j]-list1[i]
# print("Result is ",result)

# in_num=int(input("Enter the number you want to reverse."))
# num=abs(in_num)
# new_num=0
# while num>0:
#     remainder=num%10
#     new_num=new_num*10+remainder
#     num=num//10
# if in_num<0:
#     print("Reversed number is",-new_num)
# else:
#     print("Reveresed number is ",new_num)
# x=1534236469
# if (-2**31<=x<=2**31-1):
#     print("Condition satisfied")
# else:
#     print("Condition not satisfied.")


# class Solution:
#     def reverse(self, x: int) -> int:
#         if -2**31 <= x <= 2**31 - 1:
#             print("Condition satisfied.")
#             in_num=x
#             num=abs(in_num)
#             new_num=0
#             while num>0:
#                 remainder=num%10
#                 new_num=new_num*10+remainder
#                 num=num//10
#             if in_num<0:
#                 return -new_num
#             else:
#                 return new_num
#         else:
#             return 0
# obj1=Solution()
# print(obj1.reverse(1534236469))


# print(2**31-1)
# print(2147483647>1534236469)

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if -2**31<=x<=2**31-1:
#             num1=x
#             new_num=0
#             while num1>0:
#                 remainder=num1%10
#                 new_num=new_num*10+remainder
#                 num1=num1//10
#             if new_num<-2**31 or 2**31-1<new_num:return 0
#             else:
#                 if new_num!=num1 or num1<0:
#                     return "false"
#                 else:
#                     return "true"
#         else:
#             return 0
# obj1=Solution()
# print(obj1.isPalindrome(-121))


name="vishalkumarsingh"
print(name.count('a'))