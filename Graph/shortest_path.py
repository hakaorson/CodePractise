"""
输入
graph 输入的图
src 原点
返回
dis 记录源点到其他点的最短距离
path 路径
"""
import json
def dijkstra(graph,src):
  if graph ==None:
    return None
  # 定点集合
  nodes = [i for i in range(len(graph))] # 获取顶点列表，用邻接矩阵存储图
  # 顶点是否被访问
  visited = []
  visited.append(src)
  # 初始化dis
  dis = {src:0}# 源点到自身的距离为0
  for i in nodes:
    dis[i] = graph[src][i]
  path={src:{src:[]}} # 记录源节点到每个节点的路径
  k=pre=src
  while nodes:
    temp_k = k
    mid_distance=float('inf') # 设置中间距离无穷大
    for v in visited:
      for d in nodes:
        if graph[src][v] != float('inf') and graph[v][d] != float('inf'):# 有边
          new_distance = graph[src][v]+graph[v][d]
          if new_distance <= mid_distance:
            mid_distance=new_distance
            graph[src][d]=new_distance # 进行距离更新
            k=d
            pre=v
    if k!=src and temp_k==k:
      break
    dis[k]=mid_distance # 最短路径
    path[src][k]=[i for i in path[src][pre]]
    path[src][k].append(k)

    visited.append(k)
    nodes.remove(k)
    print(nodes)
  return dis,path
if __name__ == '__main__':
  # 输入的有向图,有边存储的就是边的权值，无边就是float('inf')，顶点到自身就是0
  graph = [ 
    [0, float('inf'), 10, float('inf'), 30, 100],
    [float('inf'), 0, 5, float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), 0, 50, float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), 0, float('inf'), 10],
    [float('inf'), float('inf'), float('inf'), 20, 0, 60],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0]]
  dis,path= dijkstra(graph, 0) # 查找从源点0开始带其他节点的最短路径
  print(dis)
  print(json.dumps(path, indent=4))


