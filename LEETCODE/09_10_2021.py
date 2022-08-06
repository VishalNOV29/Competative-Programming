# list1 = [1, 2, 3, 4, 5,10,20,30]
# target = int(input("Enter the number:"))
# if target in list1:
#     print("Checking if condition.")
#     print(list1.index(target))

# else:
#     Max = max(list1)
#     if target > Max:
#         print("Element should be at", len(list1))
#     else:
#         for i in range(len(list1)):
#             if list1[i]>target:
#                 print("Element should be at",i)

# list1=[1,2,3,4,4,5,5]
# val=int(input("Enter the element you want to remove."))
# num=list1.count(val)
# # for i in range(len(list1)):
# #     if list1[i]==val:
# #         list1.remove(val)
# #     print(list1,len(list1))
# for i in range(num):
#     list1.remove(val)
# print(list1,len(list1))


# list1=[0,1,1,1,2,2,3,3,4]
# i=0
# while i<len(list1)-1:
#     print("Entering while loop. i =",i)
#     print("list1[i] =",list1[i])
#     print("list1[i+1] =",list1[i+1])
#     if list1[i]==list1[i+1]:
#         print("Condition satisfied.")
#         list1.remove(list1[i+1])
#         i-=1
#     i+=1
#     print(list1)
# print(list1)

list1=[1,1,1,2,2,2,3,3,4,5,6]
# i=0
# while i<len(list1)-1:
#     print("i =",i)
#     print("Entering outer while loop.")
#     print("list1[i] =",list1[i])
#     print("list1[i+1] =",list1[i+1])
#     if list1[i]==list1[i+1]:
#         print("Condition satisfied.")
#         k=i+1
#         print("k =",i+1)
#         while k<len(list1)-1:
#             print("Entering inner loop.")
#             print("k =",k)
#             if list1[k]==list1[k+1]:
#                 print("list1[k] =",list1[k])
#                 print("list1[k+1] =",list1[k+1])
#                 list1.remove(list1[k+1])
#                 # print(list1)
#                 k-=1
#             k+=1
#             print("list1 after inner if termination ",list1)
#         i+=1
#         print("list1 after inner loop termination",list1)
#     i+=1
#     print("list1 after outer if termination. ",list1)
# print("final list1 ",list1)

list1=[0,0,1,1,1,1,2,3,3]
i=0
while i<len(list1)-1:
    print("Entering outer while loop.")
    print("i =",i)
    if list1[i]==list1[i+1]:
        print("Condition satisfied.")
        k=i+1
        if k==len(list1)-1:
            break
        print("k =",k)
        while list1[i]==list1[k]:
            print("Entering inner loop.")
            print("list1[k] =",list1[k])
            print("list1[k+1] =",list1[k+1])
            if list1[k]==list1[k+1]:
                print("Condition satisfied.")
                list1.remove(list1[k+1])
                k-=1
                i+=1
                print(list1)
            else:
                print("Condition not satisfied breaking inner loop.")
                break
            k+=1
    i+=1
print(list1)
