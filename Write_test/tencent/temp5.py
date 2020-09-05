# links = [[1, 2], [3, 4], [5, 6], [1, 6]]


def kuruste(links):
    all_nodes = []
    for item in links:
        all_nodes.append(item[0])
        all_nodes.append(item[1])
    all_nodes = list(set(all_nodes))
    sorted(all_nodes)
    node_maps = {}
    for index, node in enumerate(all_nodes):
        node_maps[node] = index
    edge_list = [[node_maps[item[0]], node_maps[item[1]]]for item in links]
    union_set = [-1 for _ in range(len(all_nodes))]
    temp_result = [1 for _ in range(len(all_nodes))]

    def find_root(vertex, depth):
        if union_set[vertex] == -1:
            return(vertex, depth)
        else:
            return(find_root(union_set[vertex], depth+1))
    result = 0
    for v0, v1 in edge_list:
        v0_root, v0_depth = find_root(v0, 1)
        v1_root, v1_depth = find_root(v1, 1)
        if v0_root != v1_root:
            if v0_depth > v1_depth:
                union_set[v1_root] = v0_root
                temp_result[v0_root] += temp_result[v1_root]
                temp_result[v1_root] = 0
                result = max(result, temp_result[v0_root])
            else:
                union_set[v0_root] = v1_root
                temp_result[v1_root] += temp_result[v0_root]
                temp_result[v0_root] = 0
                result = max(result, temp_result[v1_root])
    return result


n = int(input())
for i in range(n):
    m = int(input())
    links = []
    for j in range(m):
        links.append(list(map(int, input().split())))
    result = kuruste(links)
    print(result)
# temp = kuruste(links)
