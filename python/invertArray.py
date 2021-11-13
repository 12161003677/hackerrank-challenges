#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'invertArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def invertArray(a):
    length = len(a)/2
    l = round(length)
    if length-l<0:
        l-=1
    for i in range(l):
        j = (len(a)-1)-i
        x = a[i]
        a[i] = a[j]
        a[j] = x
    
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = invertArray(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
