#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    ct=0
    for i in a:
        if i <= 0:
            ct = ct+1
    print(ct)
    if ct < k:
        x="YES"
    else :
        x = "NO"
    print(x)
    return x


k=int(input())
a=list(map(int,input().split()))
angryProfessor(k,a)
