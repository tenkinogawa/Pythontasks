import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # s = str(s)
    # name = s.title()
    # return name
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
