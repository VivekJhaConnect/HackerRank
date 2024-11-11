#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    new_arr = arr[::-1]
    
    print(f"{' '.join(map(str, new_arr))}")