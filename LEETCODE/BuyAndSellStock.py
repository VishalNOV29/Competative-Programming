# stock=[7,1,5,3,6,4]
# stock=[7,6,4,3,1]
# def myFun(arr):
#     max_profit=0
#     for i in range(len(arr)-1):
#         profit=0
#         buy=arr[i]
#         for j in range(i+1,len(arr)):
#             sell=arr[j]
#             profit=sell-buy
#             if max_profit<profit:
#                 max_profit=profit
#             if profit<0:
#                 profit=0
#                 break
#     return max_profit
# print(myFun(stock))
# for i in range()
# m=min(stock)
stock=[7,1,5,3,6,4]
aux_arr=[0]
# print(max(aux_arr))
for i in range(len(stock)-1,-1,-1):
    if stock[i]>max(aux_arr):
        aux_arr.insert(0,stock[i])
    else:
        aux_arr.insert(0,max(aux_arr))
# print(aux_arr)
aux_arr.pop()
print(aux_arr)
max_profit=0
for i in range(len(stock)):
    profit=aux_arr[i]-stock[i]
    print(profit)
    if profit>max_profit:
        print("condition satisfied.")
        max_profit=profit
        print(max_profit)
print(max_profit)


