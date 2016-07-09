# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-09 10:31:13
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-09 10:34:30
# @Email: liangchaowu5@gmail.com

# Definition of ListNode
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_curr_element(node):
    if node.next == None:
        node = None
    else:
        node.val = node.next.val
        node.next = node.next.next