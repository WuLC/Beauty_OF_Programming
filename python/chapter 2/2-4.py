# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-24 12:47:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-24 14:44:59
# @Email: liangchaowu5@gmail.com

########################################################################################
# given number n, return the number of 1 that appear in the number array [0,1,2,3.....n]
# ######################################################################################


def number_of_1(num):
    if num < 0:
        return 0
    count = 0
    s = str(num)
    n = len(s)
    for i in xrange(n):
        upper = 0 if i==0 else int(s[:i])
        lower = 0 if i==n-1 else int(s[i+1:])
        if s[i] == '0':
            count += upper*pow(10,n-i-1)
        elif s[i] == '1':
            count += upper*pow(10, n-i-1) + lower + 1
        else:
            count += (upper+1)*pow(10, n-i-1) 