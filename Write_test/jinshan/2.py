
'''
3 5 6 -1 -1 2 7 -1 -1 4 -1 -1 1 9 -1 -1 8 -1 -1
5 1
'''
# nums = list(map(int, input().split()))
# a, b = list(map(int, input().split()))
nums = [-1, 3, 5, 6, -1, -1, 2, 7, -1, -1, 4, -1, -1, 1, 9, -1, -1, 8, -1, -1]
a, b = 5, 1


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def deserialize(data):
    res = TreeNode(0)
    stack = [res]
    visited = set()
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


tree = deserialize(nums)


def find(root, p, q):
    if not root or root.val == p or root.val == q:
        return root
    left = find(root.left, p, q)
    right = find(root.right, p, q)
    if not left and not right:
        return None
    elif not left:
        return right
    elif not right:
        return left
    else:
        return root


result = find(tree, a, b)
print(result.val)
