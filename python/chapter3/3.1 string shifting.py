# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-07 22:32:07
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-07 22:57:58
# @Email: liangchaowu5@gmail.com

# method 1, shift and change the string
def shift_str(s1, s2):
    if len(s1) < len(s2):
        return False
    count = 0
    while count < len(s1):
        if s2 in s1:
            return True
        s1 = s1[-1] + s1[:-1]
        count += 1
    return False

# method 2, judge if s2 is in s1+s1
def double_str(s1, s2):
    if len(s1) < len(s2): 
        return False
    if s2 in s1+s1:
        return True
    else:
        return False


if __name__ == '__main__':
    s1, s2 = 'AABCD', 'CDAA'
    print double_str(s1, s2)
