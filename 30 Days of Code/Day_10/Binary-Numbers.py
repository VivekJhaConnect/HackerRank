#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    binary_arr = bin(n)[2:]
    
    groups_of_ones = binary_arr.split('0')
    
    max_consecutive = max(len(group) for group in groups_of_ones)
    
    print(max_consecutive)