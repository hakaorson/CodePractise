# 通过栈反序列化
def deserialize(data):
    res = TreeNode(0)
    stack = [res]
    visited = set()#关键是通过visited操作，确定哪一些结点拥有过左孩子，只要把有左孩子的区分开来就行了
    cur = 0
    while len(stack):
        curNode = stack[-1]
        if curNode.val in visited:
            stack.pop()
            if data[cur] != -1:
                curNode.right = TreeNode(data[cur])
                stack.append(curNode.right)
        else:
            if data[cur] != -1:
                curNode.left = TreeNode(data[cur])
                stack.append(curNode.left)
            visited.add(curNode.val)
        cur += 1
    return res.right
# Definition for a binary tree node.
import queue


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root: TreeNode):
        res = []
        que = queue.Queue()
        que.put(root)
        while not que.empty():
            curNode = que.get()
            if curNode is None:
                res.append("#")
            else:
                res.append(str(curNode.val))
                que.put(curNode.left)
                que.put(curNode.right)
        return ','.join(res)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        data = ['#'] + data.split(',')
        res = TreeNode(0)
        que = queue.Queue()
        que.put(res)
        cur = 0
        while not que.empty():
            curNode = que.get()
            if data[cur] != '#':
                curNode.left = TreeNode(int(data[cur]))
                que.put(curNode.left)
            if data[cur+1] != '#':
                curNode.right = TreeNode(int(data[cur+1]))
                que.put(curNode.right)
            cur += 2
        return res.right


# root = TreeNode(4)
# root.right = TreeNode(1)
# root.left = TreeNode(3)
# root.left.left = TreeNode(2)
# res = Codec().serialize(root)
# Codec().deserialize(res)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))