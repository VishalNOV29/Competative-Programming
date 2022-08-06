# num_arr=list(map(int,input("Enter array: ").strip().split()))
# print(2%5)
# num_list=[1,2,3,4]
# length=len(num_list)-1
# num=0
# for i in range(length,-1,-1):
#     num+=num_list[length-i]*(10**i)
#     print("num =",num)
# print(num)



# class Fruits:
#     def __init__(self):
#         print("Object is created.")

#     def firstMethod(self):
#         print("This is the first method.")

#     def secondMethod(self):
#         self.firstMethod()  # calling first method in second method.
#         print("This is second method")


# obj = Fruits()
# obj.secondMethod()


# arr=[1,2,3,4,5,6,7,8]
# k=11
# i=0
# j=len(arr)-1
# Sum=0
# def myFun(arr,k):
#     i=0
#     j=len(arr)-1
#     while (i<j):
#         result=arr[i]+arr[j]
#         if result==k:
#             return i,j
#         elif result<k:
#             i+=1
#         elif result>k:
#             j-=1
#     return "elements not found"
# print(myFun(arr,k))

# k=3
# arr=[1,2,3,4,5,6,7,8]
# arr=[2,1,5,1,3,2]
# # arr=[1,9,-1,-2,7,3,-1,2]
# arr=[1,2,3]
# i=0
# j=k
# Sum=0
# while (j<=len(arr)):
#     print("i =",i)
#     print("j =",j)
#     temp=sum(arr[i:j])
#     if temp>Sum:
#         Sum=temp
#     i+=1
#     j+=1
# print(Sum)

# from dis import dis


# arr=[1,8,6,2,5,4,8,3,7]
# # arr=[1,1]
# i=0
# j=len(arr)-1
# area=0
# while (i!=j):
#     distance=j-i
#     print("distance =",distance)
#     temp_area=None
#     # area=distance*min(arr[i],arr[j])
#     if arr[i]<arr[j]:
#         temp_area=distance*arr[i]
#         i+=1
#     elif arr[i]>arr[j]:
#         temp_area=distance*arr[j]
#         j-=1
#     else:
#         print("Both pillars are equal.",i,j)
#         temp_area=distance*arr[i]
#         i+=1
#     if area<temp_area:
#         area=temp_area
# print(area)

# arr=[-1,0,1,2,-1,-4]
# arr.sort()
# print(arr)

# arr=['o','p','a']
# # print(arr.sort())
# arr.sort()
# print(arr)

# string="bcajdfklsfhpahsffioahfsflkdfklhasdjfahlagflajdabc"
# string=set(string)
# string=list(string)
# string.sort()
# print("".join(string))
# string="abcdfghijklops"
# string1="adfhpioklsgjbc"
# print(string>string1)

class Stack:
    def __init__(self):
        stack=[]
    def empty(self):
        return len(self.stack==0)
    def push(self,ele):
        self.stack.append(ele)
    def pop(self):
        self.stack.pop()
        if self.stack.self.empty():
            return "EMPTY"
    def inc(self,data1,data2):
        
