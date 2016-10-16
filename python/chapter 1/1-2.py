# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-16 20:37:18
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-16 22:03:42
# @Email: liangchaowu5@gmail.com


# method 1
# use the trick of going through a m*n matrix with an integer
# expand 3*3 area to m*n area

m, n = 3, 3
i = pow(m*n,2) - 1
while i >= 0:
    #print i/(m*n), i%(m*n)
    if i/(m*n)%n != i%(m*n)%n:
        print 'A=%s, B=%s'%(i/(m*n)+1, i%(m*n)+1)
    i -= 1
    
