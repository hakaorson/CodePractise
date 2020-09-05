

class BaseNode():
    def __init__(self, val, childrens):
        self.val = val
        self.childrens = childrens


base_struct = {}
input_str = input()
all_nodes = input_str.split('|')
for node in all_nodes:
    node_name, node_val, childrens = node.split('`')
    childrens = childrens.split(',')
    node_val = int(node_val)
    base_struct[node_name] = BaseNode(node_val, childrens)


def getmax(name):
    if name == 'END':
        return 0
    childrens = base_struct[name].childrens
    temp_mac = 0
    for child in childrens:
        temp_mac = max(temp_mac, getmax(child))
    return base_struct[name].val+temp_mac


result = getmax('HEAD')
print(result)
