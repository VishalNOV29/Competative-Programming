# arr1=[1,2]
# arr2=[3,4]
# arr3=arr1+arr2
# print(arr3)
# length=len(arr3)
# if length%2!=0:
#     print(arr3[(length//2)+1])
# else:
#     first=arr3[length//2]
#     second=arr3[(length//2)-1]
#     m=(first+second)/2
#     result=float("%.5f"%m)
#     print(result)
#     print(type(result))

# list1=['vishal','kumar','singh','rajput','jhakhara']
# i=0
# while True:
#     common=""
#     for i in range()
# print(2+++++++++2)
# n=int(input("Enter the number: "))
# def check(n):
#     for i in range(2,n//2+1):
#         if n%i==0:
#             return True
#     return False

# print(check(n))
# for num  in range(2,n):
#     if num%2==0 or num%3==0 or num%5==0 or num%7==0:
#         print("Not a prime ")
#     else:
#         print("Prime")
# def checkPrime(n):
#     if n==1:
#         return False
#     for i in range(2,n):
#         if n==2 or n==3 or n==5:
#             print("Condition1 satisfied.")
#             return True
#         if n%2==0 or n%3==0 or n%5==0 or n%7==0:
#             return False
#     return True
# num=int(input("Enter nuber of elements."))
# print(checkPrime(num))

# print(0%2)
# num=int(input("Enter a number: "))
# count=0
# for i in range(2,num):
#     if num%i==0:
#         count+=1
# print(count)


# (a).
def myFun1(num1):
    # base case for recursive function given in the question (S1=1).
    if num1 == 1:
        return 1
    else:
        return num1/(myFun1(num1-1))  # recursive function.


print("Output of first question---------------------------------")
num1 = int(input("Enter num1 for first function: "))
print(f"{num1}th term =", myFun1(num1))

# (b).


def myFun2(num2):
    # first base case (S0=3).
    if num2 == 0:
        return 3

    # second base case (S1=4).
    if num2 == 1:
        return 4
    else:
        return (3*myFun2(num2-2)-5)  # recursive function.


print("Output of second question---------------------------------")
num2 = int(input("Enter number for second function: "))
print(f"{num2}th term =", myFun2(num2))


# (c).
def myFun3(num3):
    # first base case (S0=0)
    if num3 == 0:
        return 0
    # second base case (s1=1)
    if num3 == 1:
        return 1
    else:
        return (3*myFun3(num3-1)-myFun3(num3-2))  # recursive function.


print("Output of thied question--------------------------------------")
num3 = int(input("Enter number for third function: "))
print(f"{num3}th term =", myFun3(num3))
