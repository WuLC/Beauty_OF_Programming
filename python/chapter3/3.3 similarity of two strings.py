# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-09 09:55:31
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-09 10:30:15
# @Email: liangchaowu5@gmail.com

# classical problem in NLP: weight minimum edit distance 

# dynamic programming
def similarity_of_strings(s1, s2):
    dp = [[0 for j in xrange(len(s2)+1)] for i in xrange(len(s1)+1)]
    for i in xrange(len(s1)+1):
        for j in xrange(len(s2)+1):
            if i==0 and j==0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = dp[i][j-1] + 1 # add to s1
            elif j == 0:
                dp[i][j] = dp[i-1][j] + 1 # delete from s1
            else:
                add_distance = dp[i][j-1] + 1
                delete_distance = dp[i-1][j] + 1
                modify_distance = dp[i-1][j-1] if s1[i-1] == s2[j-1] else dp[i-1][j-1]+1 # modify s1[i-1]
                dp[i][j] = min(add_distance, delete_distance, modify_distance)
    if dp[len(s1)][len(s2)] == 0:
        return 1
    else:
        return 1/dp[len(s1)][len(s2)]

