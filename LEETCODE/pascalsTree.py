n=int(input("Enter the number: "))
pascal_triangle=[]
prev_list=[]
for i in range(n):
    print("i =",i)
    print("prev_list =",prev_list)
    current_list=[]
    for j in range(i+1):
        print("j =",j)
        if j==0:
            current_list.append(1)
        elif j==i:
            current_list.append(1)
        else:
            print("i =",i,"j =",j)
            current_list.append(prev_list[j-1]+prev_list[j])
    prev_list=current_list
    print("current_list =",current_list)
    pascal_triangle.append(prev_list)
    current_list=[]
    print("pascle_triangle =",pascal_triangle)
print(pascal_triangle)

