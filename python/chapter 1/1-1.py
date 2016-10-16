# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-10-16 12:27:57
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-16 20:35:05
# @Email: liangchaowu5@gmail.com

########################################
# take up certain usage  of a cpu cor
#########################################

import time
import psutil

# for CPU with n cores, a dead loop can  take up(100/n)%  of CPU usage
def take_up_a_core():
    i = 0
    while True:
        i += 1


# 260000 loops will take up about 50% of a CPU of 2.4GHz
# without system call, just caculate the number of loops based on the frequency of CPU and number of instructions of statement
# pay attention the instructions of for statement in python is different from that in C, and CPython is used in this test
def take_up_half():
    while True:
        for i in xrange(260000):
            pass
        time.sleep(0.01)



# take up certain percent with psutil, only apply to single-core CPU, default 50%
def take_up_certain_percent(percent = 50):
    i = 0
    while True:
        while (psutil.cpu_percent() > percent):
            time.sleep(0.01)
        i += 1


if __name__ == '__main__':
    take_up_certain_percent()