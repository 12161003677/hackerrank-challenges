#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    sumMainDiagonal = 0
    sumSecondaryDiagonal = 0
    for i, i_val in enumerate(arr):
        for j, j_val in enumerate(arr[i]):            
            if i == j:
                sumMainDiagonal += j_val
            if i+j == n-1:
                sumSecondaryDiagonal += j_val
    return abs(sumMainDiagonal - sumSecondaryDiagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
