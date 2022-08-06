# list1=[1,3]
# k=int(input("Enter the numebr"))
# # list2=[]
# count=0
# for i in range(len(list1)):
#     for j in range(i,len(list1)):
#         if abs(list1[i]-list1[j])==k:
#             # new_list1=[i,j]
#             # list2.append(new_list1)
#             count+=1
# print(list2)
# print(len(list2))

name=input("Enter the name you want to enter.")
check=0
count=0
ele_list=[]
for i in range(len(name)):
    new_ele=name[i:i+3]
    if len(new_ele)==3:
        ele_list.append(new_ele)
for ele in ele_list:
    for element in ele:
        if ele.count(element)==1:
            check=1
        else:
            check=0
            break
    if check==1:
        count+=1        
print(count)