# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-07 22:59:51
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-08 23:33:46
# @Email: liangchaowu5@gmail.com



nums ={
    0: '',
    1: '',
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'xyz'
}

# method 1, no recursive
def method1(num):
    posi = [0 for i in xrange(10)]
    result = []
    while True:
        tmp = ''
        for s in num:
            if s in ['0', '1']:
                continue
            n = int(s)
            tmp += nums[n][posi[n]]
        if tmp:
            result.append(tmp)
        k = len(num) - 1
        while k >= 0:
            n = int(num[k])
            if posi[n] < len(nums[n])-1:
                posi[n] += 1
                break
            else:
                posi[n] = 0
                k -= 1
        if k < 0:
            break
    return result


# method 2, recursive
def method2(num):
    result = []
    helper(num, 0, '', result)
    return result

def helper(num, index, tmp, result):
    if index == len(num):
        result.append(tmp)
        return
    n = int(num[index])
    if n in [0, 1]:
        helper(num, index+1, tmp, result)
    else:
        for i in xrange(len(nums[n])):
            helper(num, index+1, tmp+nums[n][i], result)


if __name__ == '__main__':
    r1, r2 = set(method1('12345')), set(method2('12345'))
    print r1, len(r1)
    print r2, len(r2)



