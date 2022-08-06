# Given a sorted array find the number of pairs which have a sum equal to k.
# arr=[1,4,4,5,5,6,11]
arr=[1,2,3,4]
k=5
i=0
j=len(arr)-1
count=0
while (i<j):
    print("Outside the loop",i,j)
    Sum=arr[i]+arr[j]
    if Sum==k:
        count+=1
        print(i,j)
        i+=1
        j-=1
    elif Sum>k:
        j-=1
    else:
        i+=1
print(count)