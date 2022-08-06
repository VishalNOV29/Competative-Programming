# def countAndSay(num):
#     if num==1:
#         return "1"
#     else:
#         res=countAndSay(num-1)
#         list1=list(res)
#         set_list=[]
#         for ele in list1:
#             if ele not in set_list:
#                 set_list.append(ele)
#         myStr=""
#         for ele in set_list:
#             c=list1.count(ele)
#             myStr=myStr+str(c)+str(ele)
#         # res=myStr
#         return myStr
# res=countAndSay(4)
# print(res)
# class Hello:
#     def countAndSay(self,n):
#         if n==1:
#            return "hello"
#         else:
#             return self.countAndSay(n-1)

# obj=Hello()
# res=obj.countAndSay(4)
# print(res)

# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n==1:
#             return "1"
#         else:
#             res=self.countAndSay(n-1)
#             list1=list(res)
#             set_list=[]
#             for ele in list1:
#                 if ele not in set_list:
#                     set_list.append(ele)
#             myStr=""
#             for ele in set_list:
#                 c=list1.count(ele)
#                 myStr=myStr+str(c)+str(ele)
#             return myStr
# obj=Solution()
# result=obj.countAndSay(4)
# print(result)

# string="1111222233344456778"
# list1=list(string)
# i=0
# myStr=""
# while i<len(list1):
#     ele=list1[i]
#     j=i+1
#     count=1
#     if j>=len(list1):
#         myStr=myStr+str(count)+str(ele)
#         break
#     while list1[j]==ele:
#         count+=1
#         j+=1
#         if j>=len(list1):
#             break
#     myStr=myStr+str(count)+str(ele)
#     i=j
# print(myStr)
# from numpy import insert
# from pandas import interval_range


# intervals = [[1,4],[3,6],[2,8]]
# # intervals=[[1,2],[1,4],[3,4]]
# intervals.sort()
# print("Sorted",intervals)
# length=len(intervals)
# i=1
# while i<length:
#     print("Entering the loop.")
#     print("intervals[i] =",intervals[i])
#     if intervals[i][1]<=intervals[i-1][1]:
#         print("Condition1 satisfied.")
#         intervals.pop(i)
#         length-=1
#         i-=1
#     i+=1
# i=1
# while i<length:
#     print("Entering the loop.")
#     print("intervals[i] =",intervals[i])
#     if intervals[i][1]>=intervals[i-1][1] and intervals[i][0]==intervals[i-1][0]:
#         print("Condition1 satisfied.")
#         intervals.pop(i-1)
#         length-=1
#         i-=1
#     i+=1
# print(intervals)
print("Right shift")
for i in range(10):
    print(i,i>>1)
print("Left shift")
for i in range(10):
    print(i,i<<1)