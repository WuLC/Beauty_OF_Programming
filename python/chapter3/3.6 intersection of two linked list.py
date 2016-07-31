# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-31 07:59:49
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-31 08:43:29
# @Email: liangchaowu5@gmail.com

# definition of a ListNode
class ListNode():
    def __init__(self, val):
        self.next = None
        self.val = val


# method 1, judge whether two linked list has the same tail
def is_intersect(head1, head2):
    if head1 == None or head2 == None:
        return False
    end1, end2 = head1, head2
    while end1.next:
        end1 = end1.next
    while end2.next:
        end2 = end2.next
    return end1 == end2  # this will check the address of two instance,__eq__() function


# method 2, hash table
def is_intersect(head1, head2):
    if head1 == None or head2 == None:
        return False
    nodes = set()
    while head1:
        nodes.add(head1)
        head1 = head1.next
    while head2:
        if head2 in nodes:
            return True
        head2 = head2.next
    return False


# method 3, link the tail of one linked list to the head of another and judge whether there is a loop
def is_intersect(head1, head2):
    if head1 == None or head2 == None:
        return False
    tail = head1
    while tail.next:
        tail = tail.next
    tail.next = head2
    p = head2
    while p.next:
        if p.next == head2:
            p.next = None
            return True
        p = p.next
    return False
