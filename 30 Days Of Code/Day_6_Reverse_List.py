import math
import os
import random
import re
import sys

n = int(input("Type your Input:"))

arr = list(map(int, input().rstrip().split()))
print("Input is ".join(map(str, arr[::-1])))
