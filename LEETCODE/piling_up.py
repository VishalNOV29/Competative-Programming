# from inspect import stack

t=int(input())
for i in range(t):
    num=int(input())
    arr=list(map(int,input("Enter the numbers separated by space: ").strip().split()))
    stack=[]
    while True:
        if len(stack)==0:
            first_ele=arr[0]
            second_ele=arr[len(arr)-1]
            if first_ele>second_ele:
                stack.append(arr.pop(0))
                # stack.append(arr.pop(len(arr)-1))
            else:
                stack.append(arr.pop(len(arr)-1))
                # stack.append(arr.pop(0))
        else:
            stack_top=stack[len(stack)-1]
            first_ele=arr[0]
            second_ele=arr[len(arr)-1]
            if first_ele<=stack_top and second_ele<=stack_top:
                if first_ele>second_ele:
                    stack.append(arr.pop(0))
                    # stack.append(arr.pop(len(arr)-1))
                else:
                    stack.append(arr.pop(len(arr)-1))
                    # stack.append(arr.pop(0))
            else:
                break
        if len(arr)==0:
            break
    print(arr)
    print(stack)
    if len(arr)==0:
        print("Yes")
    else:
        print("No")