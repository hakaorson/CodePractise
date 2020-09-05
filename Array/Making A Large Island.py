class Solution:

    def largestIsland(self, grid):
        size = len(grid)
        self.rootmap = [0 for _ in range(size*size)]
        graph_size = [0 for _ in range(size*size)]
        final_result = 0
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 1:
                    index = i*size+j
                    self.rootmap[index] = -1
                    graph_size[index] = 1
                    final_result = max(final_result, 1)
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        left_root = self.find_root(index-1)
                        self.rootmap[left_root] = index
                        graph_size[index] = graph_size[left_root] + \
                            graph_size[index]
                        graph_size[left_root] = 1
                        final_result = max(final_result, graph_size[index])
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        up_root = self.find_root(index-size)
                        self.rootmap[up_root] = index
                        graph_size[index] = graph_size[up_root] + \
                            graph_size[index]
                        graph_size[up_root] = 0
                        final_result = max(final_result, graph_size[index])
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 0:
                    index = i*size+j
                    result = set()
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        result.add(self.find_root(index-size))
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        result.add(self.find_root(index-1))
                    if i+1 < size and grid[i+1][j] == 1:
                        result.add(self.find_root(index+size))
                    if j+1 < size and grid[i][j+1] == 1:
                        result.add(self.find_root(index+1))
                    if len(result) == 2:
                        a = result.pop()
                        b = result.pop()
                        final_result = max(
                            final_result, graph_size[a]+graph_size[b]+1)
                    if len(result) == 1:
                        final_result = max(
                            final_result, graph_size[result.pop()]+1)
                    if len(result) == 0:
                        final_result = max(final_result, 1)
        return final_result

    def find_root(self, index):
        while self.rootmap[index] != -1:
            index = self.rootmap[index]
        return index


solu = Solution()
solu.largestIsland([[1]])
