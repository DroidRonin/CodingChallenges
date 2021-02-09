#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr, i, j):
    add = 0
    add += arr[i-1][j-1]
    add += arr[i-1][j]
    add += arr[i-1][j+1]
    add += arr[i][j]
    add += arr[i+1][j-1]
    add += arr[i+1][j]
    add += arr[i+1][j+1]
    return add

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maxVal = -63
    
    for i in range(1,5):
        for j in range(1,5):
           sum_= hourglassSum(arr, i, j)
           if sum_ > maxVal:
            maxVal = sum_ 
            
    result = maxVal


    fptr.write(str(result) + '\n')

    fptr.close()
