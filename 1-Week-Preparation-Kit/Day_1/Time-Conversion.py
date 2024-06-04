#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2:] == "PM" and s[:2] == "12":
        return f"{s[:-2]}"
    elif 'PM' in s:
        return f"{int(s[:2])+12}{s[2:-2]}"
    if ('AM' in s) and (s[:2] == '12'):
        return f"00{s[2:-2]}"
    else:
        return f"{s[:-2]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
