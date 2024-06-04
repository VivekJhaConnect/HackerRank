#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count = {"positive":0, 'negative':0, 'zero':0}
    for i in arr:
        if i == 0:
            count['zero'] = count['zero'] + 1
        elif i > 0:
            count['positive'] = count['positive'] + 1
        else:
            count['negative'] = count['negative'] + 1
            
    print(format(count['positive']/len(arr), '.6f'))
    print(format(count['negative']/len(arr), '.6f'))
    print(format(count['zero']/len(arr), '.6f'))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
