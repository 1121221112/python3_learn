# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 237. 删除链表中的节点
        node.val = node.next.val
        node.next = node.next.next

    def getDecimalValue(self, head: ListNode) -> int:
        # 1290. 二进制链表转整数
        cur = head
        ans = 0
        while cur:
            ans = ans * 2 + cur.val
            cur = cur.next
        return ans
