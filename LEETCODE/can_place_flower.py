from sre_constants import CATEGORY_UNI_NOT_LINEBREAK


arr = [1, 0, 0, 0, 1]
n = 2
# print("Before loop")
# for i in range(1, len(arr)):
#     print("Entered in the for loop.")
#     if i == len(arr)-1:
#         if arr[i] == 0 and arr[i-1] == 0 and n != 0:
#             n -= 1
#             arr[len(arr)-1] = 1
#             print("condition satisfied, i=", i)

#     elif arr[i-1] == 0 and arr[i+1] == 0 and arr[i] != 1:
#         arr[i] = 1
#         n -= 1
#         print("condition satisfied, i=", i)

# print("After loop")
# if n==0:
#     print("True",n)
#     print(arr)
# else:
#     print("False",n)
# def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
#     arr = flowerbed
#     for i in range(1, len(arr)):
#         if i == len(arr)-1:
#             if arr[i] == 0 and arr[i-1] == 0 and n != 0:
#                 n -= 1
#                 arr[len(arr)-1] = 1
#         elif arr[i-1] == 0 and arr[i+1] == 0 and arr[i] != 1:
#             arr[i] = 1
#             n -= 1
#         if n == 0:
#             return "true"
#         else:
#             return "false"
# print(canPlaceFlowers(arr,n))


# check=[[1,3],[1,4],[2,3],[2,4],[4,3]]
# check=[[1,2],[2,3]]

# list1=[ele[0] for ele in check]
# list2=[ele[1] for ele in check]
# print(list1)
# print(list2)
# set1=set(list1)
# set2=set(list2)
# print(set1)
# print(set2)
# print(set2-set1)
# if set1-set2:
#     print("ture")


# class Solution:
#     def myfun(self,string):
#         print("this method is being called.")
#         class Stack:
#             def __init__(self):
#                 self.stack=[]
#                 self.top=-1
#             def push(self,data):
#                 self.stack.append(data)
#                 self.top+=1
#             def pop(self,data):
#                 self.stack.remove(data)
#                 self.top-=1
#             def display(self):
#                 while self.top>=0:
#                     print(self.stack[self.top])
#                     self.top-=1
#             def is_empty(self):
#                 return self.top==-1
#             def peak(self):
#                 return self.stack[self.top]
#         obj=Stack()
#         parans=string
#         parans=list(parans)[1:len(parans)-1]
#         invalid=0
#         print("Going inside the for loop.")
#         for ele in parans:
#             print("Entering the for loop.")
#             if ele=="(" or ele=="{" or ele=="[":
#                 print("ele =",ele)
#                 obj.push(ele)   
#                 print("ele is pushed into the stack.")
#                 print("Stack =",obj.stack)
#             else:
#                 if obj.is_empty():
#                     invalid=1
#                     break
#                 elif ele==")":
#                     print("ele =",ele)
#                     if obj.peak()=="(":
#                         obj.pop("(")
#                         print("opposite is found. popped from the stack.")
#                         print("stack =",obj.stack)
#                     else:
#                         print("opposite is not found.")
#                         invalid=1
#                         break
#                 elif ele=="]":
#                     print("ele =",ele)
#                     if obj.peak()=="[":
#                         print("opposite is found, popped from stack ")
#                         obj.pop("[")
#                         print("stack =",obj.stack)
#                     else:
#                         # print("false")
#                         invalid=1
#                         break
#                 elif ele=="}":
#                     print("ele =",ele)
#                     if obj.peak()=="{":
#                         obj.pop("{")
#                         print("opposite is found, popped from the stack.")
#                         print("stack =",obj.stack)
#                     else:
#                         # print("false")
#                         invalid=1
#                         break
#         if invalid==1:
#             return False
#         else:
#             if obj.is_empty():
#                 return True
#             else:
#                 return False
# obj=Solution()
# result=obj.myfun("()")
# print(result)

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack=[]
#         for ele in s:
#             if ele=="(" or ele=="{" or ele=="[":
#                 stack.append(ele)
#             else:
#                 if len(stack)==0:
#                     return False
#                 elif ele==")":
#                     if stack[len(stack)-1]=="(":
#                         stack.pop()
#                     else:
#                         return False
#                 elif ele=="]":
#                     if stack[len(stack)-1]=="[":
#                         stack.pop()
#                     else:
#                         return False
#                 elif ele=="}":
#                     if stack[len(stack)-1]=="{":
#                         stack.pop()
#                     else:
#                         return False
#         if len(stack)==0:
#             return True
#         else:
#             return False
# obj=Solution()
# a=obj.isValid("(})")
# print(a)


# arr=list(map(int,input("Enter numbers: ").strip().split()))
# pick=None
# check=0
# if len(arr)>=3:
#     i=0
#     while i<len(arr)-1:
#         if arr[i]<arr[i+1]:
#             i+=1
#         elif arr[i]>=arr[i+1]:
#             if i==0:
#                 print("Flase0")
#                 break
#             pick=arr[i]
#             print("Pick is found ",pick)
#             break
#     if pick==None:
#         print("Pick is none.")
#     else:
#         print("Pick is not none.")
#         j=i
#         while j<len(arr)-1:
#             if arr[j]>arr[j+1]:
#                 j+=1
#             elif arr[j]<=arr[j+1]:
#                 print("False2")
#                 check=1
#                 break
#         if check==0:
#             print("True.")
# else:
#     print("False3")



# name=input("Enter the string: ")
# sub_str=input("Enter the sub string: ")
# if len(name)==0:
#     print(0)
# elif sub_str in name:
#     print(name.index(sub_str))
# else:
#     print(-1)

arr=list(map(int,input("Enter numbers: ").strip().split()))
i=1
while True:
    if i in arr:
        i+=1
    else:
        print(i)
        break