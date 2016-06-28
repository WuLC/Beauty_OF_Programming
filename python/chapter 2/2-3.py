# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-16 08:39:01
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-28 21:08:46
# @Email: liangchaowu5@gmail.com

# find the number in a unsorted array, the number appearing times is over a certain percentage of the length of the array

#######################################################################
# problem1：find the number whose appearing-percentage is more than 50%
# requirements: tranverse once,constant space
#######################################################################
def solution1(nums):
    if len(nums) == 0:
        raise ValueError('not a legal array')
    candidate = nums[0]
    m = 1
    for i in xrange(1,len(nums)):
        if m == 0:
            candidate = nums[i]
        else:
            if candidate == nums[i]:
                m += 1
            else:
                m -= 1
    return candidate



#######################################################################
# problem2：find three numbers whose appearing-percentage are all over 25%
# requirements: tranverse once,constant space
#######################################################################
def solution2(nums):
    m = 3  # the number of numbers to be found
    if len(nums) < m:
        raise ValueError('not a leagal array')
    numbers = [None for i in xrange(m)]
    times = [0 for i in xrange(m)]
    for i in xrange(len(nums)):
        if nums[i] not in numbers:
            if any(num == None for num in numbers):
                for j in xrange(m):
                    if numbers[j] == None:
                        numbers[j], times[j]= nums[i], 1
                        break
            elif any(time==0 for time in times):
                for j in xrange(m):
                    if times[j] == 0: 
                        numbers[j], times[j] = nums[i], 1
                        break
            else:
                times = map(lambda x:x-1,times)
        else:
            for j in xrange(m):
                if numbers[j] == nums[i]:
                    times[j] += 1
                    break       
    return numbers


if __name__ == '__main__':
    nums1 = [1,2,3,1,5,1,6,1,1,3,1,3,1]
    print solution1(nums1)
    nums2 = [1,1,1,1,1,1,2,3,3,3,3,3,3,4,5,5,5,5,5,5]
    print solution2(nums2)
