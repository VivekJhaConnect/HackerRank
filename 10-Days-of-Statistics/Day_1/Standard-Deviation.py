#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = round(sum(arr) / len(arr))
    
    # Calculate the variance
    variance = sum((x - mean) ** 2 for x in arr) / len(arr)
    
    # Calculate the standard deviation
    std_dev = variance ** 0.5
    
    # Print the standard deviation rounded to one decimal place
    print(f"{std_dev:.1f}")

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
