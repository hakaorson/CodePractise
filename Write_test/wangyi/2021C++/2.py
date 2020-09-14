'''
10 9
1 left 2
1 right 3
2 left 4
2 right 5
3 right 6
6 left 7
6 right 8
7 left 9
7 right 10
'''
import queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


m, n = list(map(int, input().split()))
allinput = []
for i in range(n):
    allinput.append(list(input().split()))
inputindex = 0
treeroot = Node(1)
myqueue = queue.Queue()
myqueue.put(treeroot)
while not myqueue.empty():
    tempnode = myqueue.get()
    while inputindex < n and allinput[inputindex][0] == str(tempnode.val):
        if allinput[inputindex][1] == 'left':
            tempnode.left = Node(int(allinput[inputindex][2]))
            myqueue.put(tempnode.left)
        else:
            tempnode.right = Node(int(allinput[inputindex][2]))
            myqueue.put(tempnode.right)
        inputindex += 1

res = 0


def dfs(root: Node):
    if root is not None:
        dfs(root.left)
        dfs(root.right)
        if root.left and root.right and not root.left.left and not root.left.right and not root.right.left and not root.right.right:
            global res
            res += 1
    else:
        return


dfs(treeroot)
print(res)
