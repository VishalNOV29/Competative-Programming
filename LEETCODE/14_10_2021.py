k=int(input("Entet the repetition lenght: "))
string=input("Enter the string : ")
a=len(string)
Max=0
str_list=[]
valid_list=[]
for i in range(a+1-k):
    for j in range(i+k,a+1):
        new_str=string[i:j]
        print("new_str =",new_str)
        if len(new_str)>=k:
            str_list.append(new_str)
            check=0
            for ele in set(new_str):
                if new_str.count(ele)>=k:
                    print("Making check 1.")
                    check=1
                else:
                    check=0
                    print("Making check 0")
                if check==1 and len(new_str)>Max:
                    Max=len(new_str)
                    
print(str_list)
print(valid_list)
print(Max)
