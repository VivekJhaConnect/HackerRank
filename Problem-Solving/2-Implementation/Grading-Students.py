#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    grades_list = []
    for grade in grades:
        check_round = 5 - (grade % 5)
        
        if grade < 40:
            if check_round < 3 and grade + check_round == 40:
                grades_list.append(grade + check_round)
            else:
                grades_list.append(grade)
        else:
            if check_round < 3:
                grades_list.append(grade + check_round)
            else:
                grades_list.append(grade)
    return grades_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
