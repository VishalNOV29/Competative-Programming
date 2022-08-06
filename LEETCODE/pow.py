# num=int(input("Enter the number: "))
# i=0
# while True:
#     if (i*i>num):
#         print(i-1)
#         break
#     i+=1
# arr=[1,2,3,4,5,6]
# k=3
# for i in range(k):
#     ele=arr.pop(len(arr)-1)
#     arr.insert(0,ele)
# # arr.insert(0,5)
# print(arr)

# class Main:
#     def __init__(self):
#         self.list1=[]
#     def add(self,data):
#         self.list1.append(data)
#     def show(self):
#         for ele in self.list1:
#             print(ele)
# obj=Main()
# obj.add("helllo")
# obj.add("vishal")
# obj.show()
# obj2=Main()
# obj2.add("Singh")
# obj2.add("kuamr")
# obj2.show()
# arr=[1,2,3,4,5]
# for i in range(len(arr)):
#     print(arr[i])
#     ele=arr.pop(arr[i])
#     if ele in arr:
#         print("True")
# if len(arr)==0:
#     print("False")

# arr=[1,2,3,4,5,1]
# set=set(arr)
# if len(arr)==len(set):
#     print("True")
# else:
#     print("false")

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# # arr=[5,4,-1,7,8]
# # sum_list = []
# arr_sum=0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)+1):
#         new_arr=arr[i:j]
#         # arr_sum=sum(arr)
#         if arr_sum>sum(new_arr) :
#             arr_sum=sum(new_arr)
#         # print(sum(arr[i:j]))
# # print(sum_list)
# # print(max(sum_list))
# print(arr_sum)

# string=input("Enter the string: ")
# def maxSub(strign):
#     maxStr=""
#     tempStr=""
#     # for i in range(len(string)):
#     i=0
#     while i<len(strign):
#         if string[i] in maxStr:
#             tempStr=""
#             continue
#         tempStr+=string[i]
#         if len(maxStr)<len(tempStr):
#             maxStr=tempStr
#     print(maxStr)
#     return len(maxStr)
# print(maxSub(string))
# # print(maxSub(string))

# arr=[1,1,1,0,0,0,3,3,3,3,3,3,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,7,7,7]
# print("arr =",arr)
# length=len(arr)
# i=0
# while i<length:
#     j=i
#     count=0
#     while (arr[i]==arr[j]):
#         count+=1
#         if count>2:
#             count-=1
#             arr.pop(j)
#             length-=1
#             j-=1
#         j+=1
#         if j==length:
#             break
#     i=j
# print(length)
# print(arr)

# from audioop import alaw2lin


# allowed=input("Enter the allowed string: ")
# words=['ab','cd','aa','bb','cc','dd']
# count=0
# for ele in words:
#     check=1
#     for word in ele:
#         if word not in allowed:
#             check=-1
#             break
#     if check==1:
#         count+=1
# print(count)

# num=input("Enter the number: ")
# list1=list(num)
# list1.append(num)
# list1.sort()
# for i in range(len(list1)-1,-1,-1):
#     if list1[i]%2!=0:
#         print(list1[i])


# arr=[1,2,3,4,5]
# arr=[1,4,25,10,25]
# arr.sort()
# k=3
# k_sum=0
# for i in range(len(arr)):
#     print("First loop is running.")
#     if arr[i]!=i+1:
#         print("Condition matched.")
#         arr.append(i+1)
#         k_sum+=i+1
#         k-=1
#     if k==0:
#         break
# if k!=0:
#     for i in range(max(arr)+1,max(arr)+k+1):
#         arr.append(i)
#         k_sum+=i
#         k-=1
# print(arr)
# print(k_sum)

# def firstProcess():
#     arr1=list(map(int,input("Enter the array elements separated by space: ").strip().split()))
#     array_sum=sum(arr1)
#     print("Sum =",array_sum)
#     return arr1
# def secondProcess(arr):
#     Sum=0
#     for ele in arr:
#         if ele%2==0:
#             Sum+=ele
#     print("Sum of even numbers =",Sum)
# def thirdProcess(arr):
#     Sum=0
#     for ele in arr:
#         if ele%2!=0:
#             Sum+=ele
#     print("Sum of odd numbers =",Sum)


# arr=firstProcess() # It will return a list
# secondProcess(arr) # calling the second process
# thirdProcess(arr) # calling the third process.


# from mpi4py import MPI
# import time
# import multiprocessing
# start = time.perf_counter()


# def do_something():
#     print("Sleeping 1 second...")
#     time.sleep(1)
#     print("sleeping done")


# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=do_something)
#     p2 = multiprocessing.Process(target=do_something)
#     p1.start()
#     p2.start()
#     # p1.join()
#     # p2.join()

#     finish = time.perf_counter()

#     print(f"finished in {round(finish,2)}: second(s)")

# importing the multiprocessing module
# import multiprocessing

# def print_cube(num):
# 	"""
# 	function to print cube of given num
# 	"""
# 	print("Cube: {}".format(num * num * num))

# def print_square(num):
# 	"""
# 	function to print square of given num
# 	"""
# 	print("Square: {}".format(num * num))

# if __name__ == "__main__":
# 	# creating processes
# 	p1 = multiprocessing.Process(target=print_square, args=(10, ))
# 	p2 = multiprocessing.Process(target=print_cube, args=(10, ))

# 	# starting process 1
# 	p1.start()
# 	# starting process 2
# 	p2.start()

# 	# wait until process 1 is finished
# 	p1.join()
# 	# wait until process 2 is finished
# 	p2.join()

# 	# both processes finished
# 	print("Done!")


import multiprocessing

# empty list with global scope
result = []
def square_list():
    """
    function to square a given list
    """
    myList=list(map(int,input().strip().split()))
    global result
    # append squares of mylist to global list result
    for num in myList:
        result.append(num)
    # print global list result
    print("Result(in process p1): {}".format(result))

def evenSum(result):
    Sum=0
    for ele in result:
        if ele%2==0:
            Sum+=ele
    print(Sum)
def oddSum(result):
    Sum=0
    for ele in result:
        Sum+=ele
    print(Sum)
if __name__ == "__main__":

    # creating new process
    p1 = multiprocessing.Process(target=square_list)
    p2=multiprocessing.Process(target=oddSum,)

    # starting process
    p1.start()
    # wait until process is finished
    p1.join()

    # print global result list
    print("Result(in main program): {}".format(result))
