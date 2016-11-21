# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-11-21 10:42:11
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-21 11:35:59
# @Email: liangchaowu5@gmail.com

# represent decimal number as fractional number
# for instance,represent 0.a1a2...am(b1b2...bn) as fractional number
# x = 0.a1a2...am(b1b2...bn)
# 10^m*x = a1a2...am + 0.(b1b2...bn)
# thus we only need to deal with 0.(b1b2...bn)
# make y =0.(b1b2...bn)
# 10^n * y = b1b2...bn +  0.(b1b2...bn) = b1b2...bn + y 
# y = b1b2...bn/(10^n-1)
# since 10^m*x = a1a2...am + 0.(b1b2...bn) = a1a2...am + y
# x = (a1a2...am + b1b2...bn/(10^n-1)) / 10^m = (a1a2...am *(10^n-1) + b1b2...bn) / ((10^n-1)*10^m)


def gcd_3(num1, num2):
    if (num1 < num2):
        return gcd_3(num2, num1)
    if num2 == 0:
        return num1
    if num1 % 2 == 0:
        return (gcd_3(num1>>1 , num2>>1)<<1) if num2%2==0 else gcd_3(num1>>1, num2)
    else:
        return gcd_3(max(num1, num2)-min(num1, num2), min(num1, num2)) if num2 % 2 != 0 else gcd_3(num1, num2>>1)


def deicmal_to_fractional(s):
    """
    s(str): decimal number 
    return(str): fractional representation of the input deciaml number 
    """
    integer, decimal = s.split('.')
    integer = int(integer)
    if '(' in decimal: # circulation part exists in decimal number
        a, b = decimal.split('(')
        b = b[:-1] # remove ')' 
        if a == b or set(a)==set(b): # specilal cases like 0.285714(285714) and 0.3(333)
            a = '' 
        numerator = (int(a)*(pow(10, len(b)) - 1) + int(b)) if len(a) != 0  else int(b)
        denominator = (pow(10, len(b)) - 1) * pow(10, len(a))
    else:
        numerator = int(decimal)
        denominator = pow(10, len(decimal))

    gcd = gcd_3(numerator, denominator)
    numerator, denominator = numerator/gcd, denominator/gcd
    numerator += integer * denominator 
    return str(numerator)+'/'+str(denominator)

if __name__ == '__main__':
    decimal = '0.285714(285714)'
    decimal = '0.3(333)'
    print deicmal_to_fractional(decimal)