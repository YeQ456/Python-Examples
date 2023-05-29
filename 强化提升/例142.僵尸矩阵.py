# 问题描述
# 给定一个二维网络，每一个格子都有一个值，2代表墙，1代表僵尸，0代表人类。僵尸每天可以将上下左右最接近
# 的人类感染成僵尸，但不能穿墙。若将所有人类感染为僵尸需要多久？若不能则返回-1


# 示例
# 输入：
# [[0,1,2,0,0],
#  [1,0,0,2,1],
#  [0,1,0,0,0]
# ]
# 输出：2

# 输入：
# [[0,0,0],
#  [0,0,0],
#  [0,0,1]
# ]
# 输出：4


# 源码实现
import collections
class Solution:
    def zombie(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
        day = 0
        while queue:
            size = len(queue)
            day += 1
            for k in range(size):
                (i,j) = queue.popleft()
                DIR = [(1,0),(-1,0),(0,1),(0,-1)]
                for (di,dj) in DIR:
                    next_i, next_j = i + di, j + dj
                    if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                        continue
                    if grid[next_i][next_j] == 1 or grid[next_i][next_j] == 2:
                        continue
                    grid[next_i][next_j] = 1
                    queue.append((next_i, next_j))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    return -1
        return day - 1

# 主函数
if __name__ == '__main__':
    s = Solution()
    grid = [[0,0,0],
            [0,0,0],
            [0,0,1]
           ]
    print("Input: ", grid)
    print("Output: ", s.zombie(grid))


# 运行结果
# Input:  [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
# Output:  4