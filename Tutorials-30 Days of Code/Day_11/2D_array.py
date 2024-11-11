#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []
    max_value = -float('inf')
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    for i in range(0, len(arr)-2):
        for j in range(0, len(arr[0])-2):
            sum_val = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] 
                       + arr[i + 1][j + 1] 
                       + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])

            if sum_val > max_value:
                max_value = sum_val

    print(max_value)
                    
                    
