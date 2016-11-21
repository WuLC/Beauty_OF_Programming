# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-21 09:19:22
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-21 11:24:54
# @Email: liangchaowu5@gmail.com

####################################################
# Three methods to find the Greatest Common Divisor
# ##################################################

# 辗转相除法
# num1 > num2, 大整数取模时除法开销大
def gcd_1(num1, num2):
    if (num1 < num2):
        return gcd_1(num2, num1)
    return num1 if num2==0 else gcd_1(num2, num1 % num2)


# 更相减损术
# num1 > num2, 减法迭代次数太大
def gcd_2(num1, num2):
    if (num1 < num2):
        return gcd_2(num2, num1)
    if num2==0:
        return num1
    num1 -= num2
    return gcd_2(num1, num2) if num1 > num2 else gcd_2(num2, num1)


# 综合前两者
# num1 > num2
# 位移代替除法
def gcd_3(num1, num2):
    if (num1 < num2):
        return gcd_3(num2, num1)
    if num2 == 0:
        return num1
    if num1 % 2 == 0:
        return (gcd_3(num1>>1 , num2>>1)<<1) if num2%2==0 else gcd_3(num1>>1, num2)
    else:
        return gcd_3(max(num1, num2)-min(num1, num2), min(num1, num2)) if num2 % 2 != 0 else gcd_3(num1, num2>>1)

# 最小公倍数
def lcm(num1, num2):
    return num1*num2/gcd_3(num1, num2)

if __name__ == '__main__':
    print gcd_1(9999,999)
    print gcd_2(9999,999)
    print gcd_3(9999,999)



