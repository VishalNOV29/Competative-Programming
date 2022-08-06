# string=input("Enter the string.")
# result=[]
# def check(i,string):
#     if i==len(string):
#         return result
#     else:
#         fixed=string[i]
#         occurance=0
#         while string[i]==fixed and i<len(string):
#             i+=1
#             occurance+=1
#             if i==len(string):
#                 break
#         result.append(f"({fixed}, {occurance})")
#         check(i,string)
# check(0,string)
# for ele in result:
#     print(ele,end=" ")
# string=input("Enter the string: ")
# result=[]
# for i in range(len(string)):
#     j=i
#     fixed=string[i]
#     occurance=0
#     while string[j]==fixed:
#         i+=1
#         j+=1
# from re import I


# i=0
# result=[]
# string=input("Enter the string: ")
# while i<len(string):
#     fixed=string[i]
#     j=i
#     occurance=0
#     while string[j]==fixed:
#         j+=1
#         occurance+=1
#         if j==len(string):
#             break
#     result.append(f"({occurance}, {fixed})")
#     i=j
# # print(result)
# for ele in result:
#     print(ele,end=" ")
# i=0
# new_str=""
# while i<len(string):
#     j=i+4
#     new_string=string[i:j]
#     # print(new_string,end="\n")
#     new_str+=(new_string+"\n")
#     i=j
# print(new_str)

# print(oct(8))
# a=oct(8)
# print(type(a))
# a=a[2:len(a)]
# print(a)
# print(hex(8))
# print(bin(8))
n=int(input("Enter the number: "))
for i in range(n):
    print()