# # # def myFun(arr):
# # #     arr.sort()
# # #     missing=1
# # #     for i in range(len(arr)):
# # #         if arr[i]<=0:
# # #             continue
# # #         elif arr[i]==missing:
# # #             missing+=1
# # #         else:
# # #             return missing
# # #     return missing
# # # arr=[0,2,2,1,1]
# # # print(myFun(arr))

# # arr=[4,1,2,1,2]
# # # arr=[7,9,7,4,2,8,7,7,1,5]
# # # print(arr.sort())
# # arr.sort()
# # print(arr)
# # for i in range(len(arr)-1):
# #     if arr[i]!=arr[i+1]:
# #         print(arr[i])
# #         break
# # list1=[1,2,3,4]
# # list2=[1,2,3]
# # print(list1+list2)
# # print(list1-list2)
# s=input("Enter s: ")
# t=input("Enter t: ")
# # set1=set(s)
# # print(set1)
# # set2=set(t)
# # print(set2)
# # print(set2-set1)
# list1=list(s)
# print(list1)
# list2=list(t)
# print(list2)
# for ele in list1:
#     list2.remove(ele)
# print(list2)
from concurrent.futures import FIRST_COMPLETED
from types import new_class


name=['visla','kumar','singh','hello','ram','bee','ace']
result=[]
for ele in name:
    old_ele=ele
    ele=list(ele)
    check=0
    for i in range(len(ele)-1):
        new_ele=None
        for j in range(i+1,len(ele)):
            f=ele[i]
            l=ele[j]
            ele[i]=l
            ele[j]=f
            new_ele="".join(ele)
        if new_ele<old_ele:
            result.append("YES")
            check=1
            break
    if check==0:
        result.append("No")
print(result)