# 问题描述
# 在一个n * m的棋盘中，0表示空，1表示障碍物。骑士的初始位置为（0,0），若要到达(n-1, m-1)位置，骑士只能
# 从左走到右边。找出骑士到达目标位置所走的最短路径并返回其长度，若骑士无法到达，则返回-1.若骑士所在位置
# 在(x,y)，则走一步可到达以下位置：(x+1,y+2), (x-1,y+2), (x+2,y+1), (x-2,y+1)


# 示例
# 输入：[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# 输出：3
# 解释：最短路径：[0,0]->[2,1]->[0,2]->[2,3]

# 输入：[[0,1,0],[0,0,1],[0,0,0]]
# 输出：-1


# 源码实现
import sys
class Solution:
    def shortestPath(self, grid):
        n = len(grid)
        if n == 0:
            return -1
        m = len(grid[0])
        if m == 0:
            return -1
        f = [[sys.maxsize for j in range(m)] for i in range(n)]
        f[0][0] = 0
        for j in range(m):
            for i in range(n):
                if not grid[i][j]:
                    if i >= 1 and j >= 2 and f[i - 1][j - 2] != sys.maxsize:
                        f[i][j] = min(f[i][j], f[i - 1][j - 2] + 1)
                    if i + 1 < n and j >= 2 and f[i + 1][j - 2] != sys.maxsize:
                        f[i][j] = min(f[i][j], f[i + 1][j - 2] + 1)
                    if i >= 2 and j >= 1 and f[i - 2][j - 1] != sys.maxsize:
                        f[i][j] = min(f[i][j], f[i - 2][j - 1] + 1)
                    if i + 2 < n and j >= 1 and f[i + 2][j - 1] != sys.maxsize:
                        f[i][j] = min(f[i][j], f[i + 2][j - 1] + 1)
        if f[n - 1][m - 1] == sys.maxsize:
            return -1
        return f[n - 1][m - 1]

# 主函数
if __name__ == '__main__':
    nums = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    s = Solution()
    print("Input: ", nums)
    print("Output: ", s.shortestPath(nums))


# 运行结果
# Input:  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# Output:  3