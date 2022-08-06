# # low=int(input("Enter the lower value: "))
# # high=int(input("Enter the higher value: "))
# # n_low=len(low)
# # n_high=len(high)
# # low_first_index=int(str(low)[0])
# # i=n_low
# # result=[]
# # while i<=n_high:
# #     for j in range():

# name=input("Enter the name: ")
# print(name.isupper())
# print(name.istitle())

# from re import L
# class Solution:
#     def winnerSquareGame(self,n: int) -> bool:
#         stack = []
#         if n % 2 == 0:
#             for i in range(n, 0, -1):
#                 res = i**(0.5)
#                 if i % 2 == 0:
#                     stack.append("Alice")
#                     if res == int(res):
#                         stack.append("Alice")
#                         break
#                 else:
#                     stack.append("Bob")
#                     if res == int(res):
#                         stack.append("Bob")
#                         break
#         else:
#             for i in range(n, 0, -1):
#                 res = i**(0.5)
#                 if i % 2 != 0:
#                     stack.append("Alice")
#                     if res == int(res):
#                         stack.append("Alice")
#                         break
#                 else:
#                     stack.append("Bob")
#                     if res == int(res):
#                         stack.append("Bob")
#                         break
#         if stack[len(stack)-1] == "Alice":
#             return True
#         else:
            # return False
# class Solution:
#     def winnerSquareGame(self,num):
#         turn="A"
#         stack=[]
#         n=num
#         result=[]
#         while True:
#             print("Entering the  loop.")
#             res=n**(0.5)
#             print("res =",res)
#             if turn=="A" and int(res)==res:
#                 print("Its A turn")
#                 stack.append(turn)
#                 print("Stack after A turn.",stack)
#                 turn="B"
#                 num-=n
#                 result.append(n)
#                 n=num
#                 print("num after A turn",num)
#                 if num==0:
#                     break
#             elif turn=="B" and int(res)==res:
#                 print("It's B turn.")
#                 stack.append(turn)
#                 print("Stack after b turn =",stack)
#                 turn="A"
#                 num-=n
#                 result.append(n)
#                 n=num
#                 print("num after B turn: ",num)
#                 if num==0:
#                     break
#             else:
#                 print("No any condition is matched. res =",res)
#                 print("n =",n)
#                 n-=1
                
#         if stack[len(stack)-1]=="A":
#             print("Stack =",stack)
#             print("result =",result)
#             return True
#         else:
#             print("resutl =",result)
#             return False


# obj=Solution()
# print(obj.winnerSquareGame(8))
# # print(obj.stack)

# # class Solution:
# #     def winnerSquareGame(self,num):
# #         n=num
# #         res=n**(0.5)
# #         turn="alice"
# #         stack=[]
# #         while True:
# #             if turn=="alice" and res==int(res):
# #                 stack.append(turn)
# #                 turn="bob"
# #                 num-=n
# #                 n-=1
# #                 if num==0:

# #                     break
# #             elif turn=="bob" and res==int(res):
# #                 stack.append(turn)
# #                 turn="alice"
# #                 num-=n
# #                 n-=1
# #                 if num==0:
# #                     break
# #             else:
# #                 n-=1
# #         if stack[len(stack)-1]=="alice":
# #             return True
# #         else:
# #             return False
# # obj=Solution()
# # print(obj.winnerSquareGame(15))
        


# name="  visal kumar singh "
# print(name)
# print(name.strip())
# a="   +0032aa"
# print(int(a))

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         myList=list(s.strip().split())
#         # print(myList)
#         num=myList[0]
#         return num
num="123"
print(num.isdigit())