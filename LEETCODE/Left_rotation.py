# class Node:
#         def __init__(self,data):
#             self.data=data
#             self.next=None
# class Queue:
#     def __init__(self):
#         self.head=None
#     def push(self,data):
#         newNode=Node(data)
#         if self.head==None:
#             self.head=newNode
#         else:
#             temp=self.head
#             while temp.next!=None:
#                 temp=temp.next
#             temp.next=newNode
#     def delete(self):
#         temp=self.head
#         self.head=self.head.next
#         return temp.data

#     def display(self):
#         temp=self.head
#         while temp!=None:
#             print(temp.data,end="->")
#             temp=temp.next
# obj=Queue()
# # obj.push(10)
# # obj.push(20)
# # obj.push(30)
# # obj.push(40)
# # print(obj.delete())
# # obj.display()
# choice_list=list(map(int,input("Enter choices spearated by space. ").strip().split()))
# n=choice_list[0] # Number of elements in the array.
# d=choice_list[1] # number of rotation to be performed.
# ele_list=list(map(int,input("Enter elements separated by space.").strip().split()))
# for i in range(n):
#     obj.push(ele_list[i])
# print("Before deletion.")
# obj.display()
# for i in range(d):
#     ele=obj.delete()
#     obj.push(ele)
# print("After deletion.")
# obj.display()


# arr=[1,2,3,4,5,6]
# d=3
# for i in range(3):
#     ele=arr.pop(0)
#     arr.append(ele)
# print(arr)

        
# num=10
# print(num//1)
# print(int(num//1))