string=input("Enter the string.")
str_list=[]
# count=0
for i in range(len(string)):
    new_str=string[i:i+3]
    if len(new_str)==3:
        str_list.append(new_str)
print(str_list)
if len(str_list)>string.count("X"):
    print(string.count("X"))
else:
    print(len(str_list))