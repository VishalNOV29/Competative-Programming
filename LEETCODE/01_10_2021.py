# list1=[]
# for i in range(len(list1)-1):
#     k=i
#     ele=list1[i]
#     for j in range(k+1,len(list1)):
#         if
import numpy as nd
list1 = nd.array([-1, 0, 1, 2, -1, -4])
new_list1 = []
for i in range(len(list1)-2):
    k1 = i
    ele1 = list1[i]
    for j in range(k1+1, len(list1)-1):
        k2 = j
        ele2 = list1[j]
        for m in range(k2+1, len(list1)):
            k3 = m
            ele3 = list1[k3]
            if ele1+ele2+ele3 == 0:
                temp_list = [list1[k1], list1[k2], list1[k3]]
                temp_list.sort()
                new_list1.append(temp_list)
new_list2 = nd.array([])
for ele in new_list1:
    if ele not in new_list2:
        new_list2=nd.append(new_list2,ele)
print(new_list2)
