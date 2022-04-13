#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

closing_brackets = {"}": "{", "]": "[", ")": "("}


def isBalanced(s):
    s = s.rstrip()
    bracket_stack = []
    for ch in s:
        if ch in closing_brackets:
            if len(bracket_stack) == 0:
                return "NO"
            last_bracket = bracket_stack.pop()
            if last_bracket != closing_brackets[ch]:
                return "NO"
        else:
            bracket_stack.append(ch)
    if len(bracket_stack) > 0:
        return "NO"
    return "YES"


if __name__ == "__main__":
    with open(os.environ["INPUT_PATH"], "r") as f, open(os.environ["OUTPUT_PATH"], "w") as fptr:

        t = int(f.readline().strip())

        for t_itr in range(t):
            s = f.readline()

            result = isBalanced(s)

            fptr.write(result + "\n")
