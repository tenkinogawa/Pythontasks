#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Number: "))
    if n % 2 == 0:
        if  n <= 20 and n > 5:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")