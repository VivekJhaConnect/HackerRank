'''
Task:

You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.

Input Format:
A single line of input containing  space separated integers.
Example: 1 2 3 4 5 6 7 8 9

Output Format:
Print the X NumPy array.
Example: [[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

import numpy

values = input()

arr = numpy.array(values.split(), dtype=int)

reshape_arr = numpy.reshape(arr, (3,3))

print(reshape_arr)

