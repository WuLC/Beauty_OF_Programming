# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-31 08:46:16
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-31 09:59:13
# @Email: liangchaowu5@gmail.com

# implement a queue,besides the implemention of inqueue and dequeue
# the queue can also return the maximal element of the queue as fast as possible

class MaxQueue():
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self.max_in_stack = None
        self.max_out_stack = None

    def dequeue(self):
        if len(self.out_stack) == 0:
            self.max_out_stack = None
            if len(self.in_stack) == 0:
                return None
            else: # pop the elements from in_stack and push them to out_stack
                while self.in_stack:
                    in_diff = self.in_stack.pop()
                    if in_diff < 0:
                        value = self.max_in_stack 
                        self.max_in_stack = value + in_diff
                    else:
                        value = self.max_in_stack - in_diff

                    if self.max_out_stack == None:
                        self.max_out_stack = value
                    out_diff = self.max_out_stack - value
                    if out_diff < 0:
                        self.max_out_stack = value
                    self.out_stack.append(out_diff)
                self.max_in_stack = None
        
        diff = self.out_stack.pop()
        if diff < 0:
            pop_value = self.max_out_stack
            self.max_out_stack += diff
        else:
            pop_value = self.max_out_stack - diff
        return pop_value



    def inqueue(self, val):
        if self.max_in_stack == None:
            self.max_in_stack = val
            self.in_stack.append(0)
        else:
            diff = self.max_in_stack - val
            if diff < 0:
                self.max_in_stack = val
            self.in_stack.append(diff)


    def max_element(self):
        if self.max_in_stack == None and self.max_out_stack == None:
            return None
        elif self.max_out_stack == None:
            return self.max_in_stack
        elif self.max_in_stack == None:
            return self.max_out_stack
        else:
            return max(self.max_out_stack, self.max_in_stack)

if __name__ == '__main__':
    que = MaxQueue()
    print que.max_element(),que.dequeue()
    for i in xrange(10):
        que.inqueue(i)
    
    for i in xrange(10):
        print que.dequeue(),que.max_element()
    print que.dequeue(), que.in_stack, que.out_stack
    