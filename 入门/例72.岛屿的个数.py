# 问题描述
# 给一个01矩阵，0代表海，1代表岛屿，若两个1相邻，则这两个1属于同一个岛。只考虑上下左右相邻，求解不同
# 岛屿的个数


# 示例
# 输入如下矩阵：
# [
#   [1,1,0,0,0],
#   [0,1,0,0,1],
#   [0,0,0,1,1],
#   [0,0,0,0,0],
#   [0,0,0,0,1]
# ]
# 
# 输出：3


# 源码实现
from collections import deque
class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.bfs(grid, i, j)
                    islands += 1
        return islands
    
    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        grid[x][y] = False
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1,0),(0,-1),(-1,0),(0,1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y):
                    continue
                queue.append((next_x,next_y))
                grid[next_x][next_y] = False
    
    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y]

# 主函数
if __name__ == '__main__':
    nums = [
        [1,1,0,0,0],
        [0,1,0,0,1],
        [0,0,0,1,1],
        [0,0,0,0,0],
        [0,0,0,0,1]
    ]
    solution = Solution()
    print("Input: ", nums)
    print("Output: ", solution.numIslands(nums))



# 运行结果
# Input:  [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
# Output:  3