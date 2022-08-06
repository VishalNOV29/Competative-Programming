def fact(x):
    temp_fact = 1
    for i in range(1, x+1):
        temp_fact = temp_fact*i
    return temp_fact


def number_of_occurenace(x, y):
    z = fact(x+y)/(fact(x)*fact(y))
    return int(z)


n = int(input("Enter the number of stairs : "))
result = 0
if n % 2 == 0:
    no_of_2 = n//2
    no_of_1 = 0
    while no_of_2 >= 0:
        temp_result = number_of_occurenace(no_of_2, no_of_1)
        result += temp_result
        no_of_2 -= 1
        no_of_1 += 2
else:
    no_of_2 = n//2
    no_of_1 = 1
    while no_of_2 >= 0:
        temp_result = number_of_occurenace(no_of_2, no_of_1)
        result += temp_result
        no_of_2-=1
        no_of_1+=2
print("Final result is", result)
