'''
In the above example, numpy.array() is used to convert a list into a NumPy array. The second argument (float) can be used to set the type of array elements.

Task:
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.

Input Format
A single line of input containing space separated numbers.
Example :- 1 2 3 4 -8 -10

Output Format:
Print the reverse NumPy array with type float.
Example:- [-10.  -8.   4.   3.   2.   1.]
'''
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    np_arr = numpy.array(arr[::-1], dtype=float)
    return np_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)