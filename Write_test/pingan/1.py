class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# 合并两个升序链表
# @param l1 ListNode类 链表1
# @param l2 ListNode类 链表2
# @return ListNode类
#


class Solution:
    def mergeTwoLists(self, l1, l2):
        res = ListNode(0)
        cur = res
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
                cur.next = None

            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
                cur.next = None
                
        if l1 is not None:
            cur.next = l1
        else:
            cur.next = l2
        return res.next

        pass
        # write code here
