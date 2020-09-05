class Node:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None


pre = [1, 2, 4, 7, 3, 5, 6, 8]
mid = [4, 7, 2, 1, 5, 3, 8, 6]


def rebuild(pre_begin, mid_begin, size):
    if size == 0:
        return None
    root_index = mid[mid_begin:mid_begin+size].index(pre[pre_begin])+mid_begin
    left_size = root_index-mid_begin
    right_size = size-left_size-1
    root = Node(pre[pre_begin])
    root.left = rebuild(pre_begin+1, mid_begin, left_size)
    root.right = rebuild(pre_begin+1+left_size, root_index+1, right_size)
    if root.left is None and root.right is None:
        print('yezi')
    return root


result = rebuild(0, 0, len(mid))
pass
