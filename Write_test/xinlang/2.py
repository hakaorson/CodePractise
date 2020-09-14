class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 输入单链表的头节点和要删除的倒数第N个，返回删除后的头节点
# @param head ListNode类 单链表的头节点
# @param n int整型
# @return ListNode类
#


class Solution:
    def removeNthFromEnd(self, head: ListNode, n):
        # write code here
        aftercur = head
        while(n):
            aftercur = aftercur.next
            n -= 1
        begincur = head
        if aftercur is None:
            return head.next
        while aftercur.next is not None:
            begincur = begincur.next
            aftercur = aftercur.next
        begincur.next = begincur.next.next
        return head


head = ListNode(0)
cur = head
nums = [1, 2, 3, 4]
for i in nums:
    cur.next = ListNode(i)
    cur = cur.next
Solution().removeNthFromEnd(head, 5)
