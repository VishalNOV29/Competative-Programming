# name="BANANA"
# count_vowel=0
# count_conso=0
# for i in range(len(name)):
#     if name[i] in "AEIOU":
#         count_vowel+=len(name)-i
#     else:
#         count_conso+=len(name)-i
# print("Vowel =",count_vowel)
# print("Consonant =",count_conso)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    stack=[]
    for ele in operations:
        if ele[0]=="1":
            stack.append(ele[2])
        elif ele[0]=="2":
            stack.pop()
        elif ele[0]=="3":
            # print(max(stack))
            return max(stack)
    # return operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
