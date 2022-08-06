# # arr=[9,8,7,6,5,4,3,2,1]
# arr=[-1,0,1,2,-1,-4]
# target=0
# arr.sort()
# print(arr)
# result=[]
# i=0
# while i<=len(arr)-3:
#     print("Entering loop")
#     j=i+1
#     print("j =",j)
#     k=len(arr)-1
#     print("k =",k)
#     # new_target=target-arr[i]
#     while (j<k):
#         print("Entering inner loop.")
#         print("arr[i] =",arr[i])
#         print("arr[j] =",arr[j])
#         print("arr[k] =",arr[k])
#         if arr[i]+arr[j]+arr[k]==target:
#             print("condition satisfied.")
#             # result.append([i,j,k])
#             result.append([arr[i],arr[j],arr[k]])
#             j+=1
#         elif arr[i]+arr[j]+arr[k]>target:
#             print("k is decreased.")
#             k-=1
#         else:
#             print("j is increased.")
#             j+=1
#     i+=1
# print(arr)
# print(result)


# # [-4, -1, -1, 0, 1, 2]        


name="vishal kumar singh"
stack1=[]
stack2=[]
for ele in name:
    stack1.append(ele)
print(stack1)
for i in range(len(stack1)):
    stack2.append(stack1.pop())
    # print(stack1)
print(stack1)
# print(stack1.pop())
print(stack2)
print("".join(stack2))