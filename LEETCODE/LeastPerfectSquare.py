lowerbond=int(input("Enter lower bond : "))
upperbond=int(input("Enter upper bond : "))
ball_list=set()
for i in range(lowerbond,upperbond+1):
    new_num=0
    while i>0:
        remainder=i%10
        new_num+=+remainder
        # print(new_num)
        i=i//10
    print(new_num)
    ball_list.add(new_num)
# ball_set=set(ball_list)
# Max=0
# for ele in ball_set:
#     a= ball_list.count(ele)
#     if a>Max:
#         Max=a
# print(Max)
print(max(ball_list))

# my_set=set()
# my_set.add(2)
# my_set.add(3)
# print(my_set)

# lowLimit=int(input("Enter low limit : "))
# highLimit=int(input("Enter high limit : "))
# ball_set=set()
# for ele in range(lowLimit,highLimit+1):
#     new_ele=0
#     while ele>0:
#         remainder=ele%10
#         ele=ele//10
#         new_ele+=remainder
#     ball_set.add(new_ele)
# print(max(ball_set))