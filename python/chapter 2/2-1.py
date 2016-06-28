# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-11 20:30:56
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-28 21:09:02
# @Email: liangchaowu5@gmail.com
# count the number of 1 of a binary number

def method1(num):
    """count by div and mod
    
    Args:
        num (binary number): the binary number to be counted
    
    Returns:
        interger: number of 1 in the binary number
    """
    count = 0
    while num!=0:
        count += num % 2
        num /= 2
    return count


def method2(num):
    """count by bit operation,faster than method 1
    
    Args:
        num (binary number): the binary number to be counted
    
    Returns:
        interger: number of 1 in the binary number
    """ 
    count = 0
    while num!=0:
        count += (num&1)
        num >>= 1 # num = num>>1
    return count


def method3(num):
    """ the times to count is equal to the number of 1 in the binary number,
        while method1 and method2 is equal to the length of num
    
    Args:
        num (binary number): the binary number to be counted
    
    Returns:
        interger: number of 1 in the binary number
    """
    count = 0
    while num!=0:
        num = num&(num-1)
        count += 1
    return count


if __name__ == '__main__':
    a = 0b10101011
    b = 0b10010010
    print bin(a&b),bin(a|b),bin(a^b)
    print bin(a>>8),bin(a<<1)
    print 1&a,isinstance(bin(1),str)

    print method1(a)
    print method2(a)
    print method3(a)
