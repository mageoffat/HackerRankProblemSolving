#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    a = s[0]+s[1]
    if s[len(s)-2] + s[len(s)-1] == "PM":
        if a == "12":
            ans = '0'+'0'+s[2:len(s)-2]
        elif a == "11":
            ans = '2'+'3'+s[2:len(s)-2]

        elif a == "10":
            ans = '2'+'2'+s[2:len(s)-2]

        elif a == "09":
            ans = '2'+'1'+s[2:len(s)-2]

        elif a == "08":
            ans = '2'+'0'+s[2:len(s)-2]

        elif a == "07":
            ans = '1'+'9'+s[2:len(s)-2]

        elif a == "06":
            ans = '1'+'8'+s[2:len(s)-2]

        elif a == "05":
            ans = '1'+'7'+s[2:len(s)-2]

        elif a == "04":
            ans = '1'+'6'+s[2:len(s)-2]

        elif a == "03":
            ans = '1'+'5'+s[2:len(s)-2]

        elif a == "02":
            ans = '1'+'4'+s[2:len(s)-2]

        elif a == "01":
            ans = '1'+'3'+s[2:len(s)-2]
    else:
        ans = s[:len(s)-2]
    return ans

    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    
    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
