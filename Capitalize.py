#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    o=[]
    s = list(map(str,s.split(' ')))
    for i in s:
        o.append(i.capitalize())
    return ' '.join(o)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
