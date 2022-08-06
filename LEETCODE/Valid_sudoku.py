# arr=[[1,2,3],[5,6,7],[4,8,9]]
# rotated=[]
# for i in range(len(arr)):
#     # for j in range()
#     new_arr=[arr[0][i],arr[1][i],arr[2][i]]
#     # print(new_arr)
#     rotated.append(new_arr)
# import numpy as np
# arr1=np.array(arr)
# arr2=np.array(rotated)
# print(arr1)
# # arr=np.matrix(arr1)

# print(arr1.transpose())
# # print(arr)

# print(max(1,2))
# m=2
# n=3
# ele=5
# arr=[[1,2,3],[4,5,6]]
# arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# arr= [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# arr=[[1,2]]
# ele=0
# m=len(arr)
# n=len(arr[0])
# found="no"
# for i in range(m):
#     first=arr[i][0]
#     # print("first =",first)
#     last=arr[i][n-1]
#     # print("last =",last)
#     # found="no"
#     if first<=ele<=last:
#         for j in range(0,n):
#             if arr[i][j]==ele:
#                 print("True")
#                 found="yes"
#                 break
# if found=="no":
#     print("false")
#     # print(arr[i][0],arr[i][n-1])
arr = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
       ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
       ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
       ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
       ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
       ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
       ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
       ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
       ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
# arr1=arr.transpose()
# print(arr1)
# for i in range(len(arr)):
#     # print(arr[i])
#     for j in range(len(arr[0])):
#         # print(arr[i][j],end=" ")
#         ele=arr[i][j]
#         # print(type(ele))
#         if ele in "123456789" and arr[i].count(ele)!=1:
#             print("False")
# # print(type(arr))
# import numpy as np

# x = np.array([1,1,1,2,2,2,5,25,1,1])
# unique, counts = np.unique(x, return_counts=True)

# print(np.asarray((unique, counts)))

# name=input("Enter the string: ")
# name="dddccdbba"
# name=list(name)
# check=-1
# for i in range(len(name)):
#     new_name=name.pop(i)
#     print("new_name =",new_name)
#     if new_name not in name:
#         print(i)
#         check=1
#         break
#     name.insert(i,new_name)
# if check!=1:
#     print(check)

# first="aa"
# last="ab"
# last=list(last)
# check=1
# for i in range(len(first)):
#     if first[i] in last:
#         last.remove(first[i])
#     else:
#         check=-1
#         print("not")
#         break
# if check==1:
#     print("yes")

# num=123
# list2=list(str(num))
# list2.reverse()
# print(list2)
# for i in range(len(str(num))):
#     print(num%10)
#     num=num//10


# class Solution:
#     def plusOne(self, digits):
#         digits.reverse()
#         num = 0
#         for i in range(len(digits)):
#             num += digits[i]*(10**i)
#         print(num)
#         num += 1
#         new_list = []
#         for i in range(len(str(num))):
#             new_list.append(num%10)
#             num = num//10
#         return new_list
# obj=Solution()
# print(obj.plusOne([1,2,3,4]))

# class ListNode {
#       int val;
#       ListNode next;
#       ListNode(int x) {
#           val = x;
#           next = null;
#       }
#   }
 


# class Solution {
#     public boolean hasCycle(ListNode head) {
#         ListNode fast = head;
#         ListNode slow = head;
 
#         while(fast != null && fast.next != null){
#             System.out.println("fast ="+fast);
#             slow = slow.next;
#             System.out.println("last ="+last.data)
#             fast = fast.next.next;
 
#             if(slow == fast)
#                 return true;
#         }
 
#         return false;
        
#     }
# }
