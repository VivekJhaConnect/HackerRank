#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime, timedelta

def time_delta(t1, t2):
    format_str = '%a %d %b %Y %H:%M:%S %z'

    # Convert the string to a datetime object
    delta_t1 = datetime.strptime(t1, format_str)
    delta_t2 = datetime.strptime(t2, format_str)
    
    # Calculate the difference in seconds
    delta_diff = delta_t1 - delta_t2
    total_seconds = int(abs(delta_diff.total_seconds()))
        
    return str(total_seconds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
