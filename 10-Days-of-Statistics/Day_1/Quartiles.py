#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    
    # Q2 (median)
    if n % 2 == 0:
        Q2 = (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        Q2 = arr[n//2]
    
    # Q1
    lower_half = arr[:n//2] if n % 2 == 0 else arr[:n//2]
    if len(lower_half) % 2 == 0:
        Q1 = (lower_half[len(lower_half)//2 - 1] + lower_half[len(lower_half)//2]) / 2
    else:
        Q1 = lower_half[len(lower_half)//2]
    
    # Q3
    upper_half = arr[n//2:] if n % 2 == 0 else arr[n//2 + 1:]
    if len(upper_half) % 2 == 0:
        Q3 = (upper_half[len(upper_half)//2 - 1] + upper_half[len(upper_half)//2]) / 2
    else:
        Q3 = upper_half[len(upper_half)//2]
    
    return int(Q1), int(Q2), int(Q3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
