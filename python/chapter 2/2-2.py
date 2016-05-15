# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-14 01:31:44
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-15 11:02:45
# @Email: liangchaowu5@gmail.com

###############################################################
# problem1: caculate the number of 0 at the end of the number n!
###############################################################

# solution1,count the 0 that each number can generate from 1 to n
def solution1_1(n):
	count = 0
	for i in xrange(1,n+1):
		while i!=0 and i%5==0 :
			count += 1
			i /= 5
	return count


# solution2,the number equal to pow(5,n) can generate n 0
def solution1_2(n):
	count = 0
	tmp = 5
	while n >= tmp:
		count += n/tmp
		tmp *= 5
	return count



############################################################
# problem2: find the index of the first 1 of number n! 
# from  lower to higer order in the form of binary 
#############################################################
# solution1,count the 0 that each  number can generate in the form of binary
def solution2_1(n):
	count = 0 
	for i in xrange(1,n+1):
		while i%2==0 and i!=0:
			i >>= 1 # i /= 2
			count += 1
	return count


# solution2,the number equal to pow(2,n) can generate n 0
def solution2_2(n):
	count = 0 
	tmp = 2
	while n>=tmp:
		count += n/tmp
		tmp <<= 1  # i *= 2
	return count




########################################
# problem3: judge if a number is pow(2,n)
# as pow(2,n) in bianry form must be 100000000...
# thus,pow(2,n)&(pow(2,n)-1)=0
########################################
def solution3(n):
	return n&(n-1)==0
	


if __name__ == '__main__':
	print solution1_1(100)
	print solution1_2(100)
	print solution2_1(12)
	print solution2_2(12)
	for i in xrange(1000):
		if solution3(i):
			print i,