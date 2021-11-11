#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sums = []
    for key_i, i in enumerate(arr):
        summation = 0
        for key_j,j in enumerate(arr):
            if(key_j!=key_i):
                summation += j
        sums.append(summation)
    print('%d %d' %(min(sums),max(sums)))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
