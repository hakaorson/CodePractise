n, k = list(map(int, input().split()))
nums = list(input().split())
nums.pop(k-1)
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# head = ListNode(0)
# cur = head
# for num in nums:
#     cur.next = ListNode(num)
strings = " ".join(nums)
print(strings)
