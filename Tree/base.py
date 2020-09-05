import queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def get_tree(tree_num):
    new_tree_num = [0, None]+tree_num+[None]*len(tree_num)
    fake_root = TreeNode(0)
    pos_queue = queue.Queue()
    pos_queue.put(fake_root)
    num_index = 1
    while not pos_queue.empty():
        temp_node = pos_queue.get()
        if new_tree_num[num_index]:
            temp_node.left = TreeNode(new_tree_num[num_index])
            pos_queue.put(temp_node.left)
        if new_tree_num[num_index+1]:
            temp_node.right = TreeNode(new_tree_num[num_index+1])
            pos_queue.put(temp_node.right)
        num_index += 2
    return fake_root.right


tree = get_tree([-2])


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = 0
        self.deffun(root)
        return self.result

    def deffun(self, root):
        if root is None:
            return 0
        leftmax = self.deffun(root.left)
        rightmax = self.deffun(root.right)
        self.result = max(self.result, leftmax+rightmax+root.val)
        return max(leftmax, rightmax)+root.val


solu = Solution()
temp = solu.maxPathSum(tree)
pass
