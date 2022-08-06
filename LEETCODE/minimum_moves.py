# string=input("Enter the string: ")
# str_list=list(string)
# stack=[]
# paran_stack=[]
# for ele in str_list:
#     print("ele =",ele)
#     if ele not in "()":
#         print("ele is a alphabate.")
#         stack.append(ele)
#         print("stack =",stack)
#         print("paran_stack =",paran_stack)
#     else:
#         print("ele is an paranthesis.")
#         if ele=="(":
#             stack.append(ele)
#             paran_stack.append(ele)
#             print("stack =",stack)
#             print("paran_stack =",paran_stack)
#         elif ele==")":
#             if len(paran_stack)!=0:
#                 if paran_stack[len(paran_stack)-1]=="(":
#                     stack.append(ele)
#                     paran_stack.pop()
#                     print("stack =",stack)
#                     print("paran_stack =",paran_stack)
# print(paran_stack)
# print(len(paran_stack))
# while len(paran_stack)!=0:
#     print("Entered while loop")
#     stack.remove(paran_stack.pop())
# print("".join(stack))

string=input("Enter the string: ")
str_list=list(string)
stack=[]
for i in range(len(string)):
    if string[i]=="(":
        stack.append(i)
    elif string[i]==")":
        if stack:
            if string[stack[len(stack)-1]]=="(":
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
for i in range(len(stack)):
    str_list.pop(stack[i]-i)
print("".join(str_list))

