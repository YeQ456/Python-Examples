# 问题描述
# 给定骑士在棋盘上的初始位置，用一个二进制矩阵表示棋盘，0表示空，1表示有障碍物。找出到达终点的最短路线，
# 返回路线的长度。若骑士不能到达则返回-1.规则如下：骑士的位置为(x,y)，下一步可到达以下位置：(x+1,y+2)、
# (x+1,y-2)、(x-1,y+2)、(x-1,y-2), (x+2,y+1)、(x+2,y-1)、(x-2,y+1)、(x-2,y-1)


# 示例
# 输入：
# [[0,0,0],
#  [0,0,0],
#  [0,0,0]
# ]
# 起点：source = [2,0], 终点：destination = [2,2]
# 输出：2
# 解释：路线为：[2,0] -> [0,1] -> [2,2]

# 输入：
# [[0,1,0],
#  [0,0,1],
#  [0,0,0]
# ]
# 起点：source = [2,0], 终点：destination = [2,2]
# 输出：-1


# 源码实现
import collections
class Point:
    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b

DIRECTIONS = [
    (-2,-1), (-2,1), (-1,2), (1,2),
    (2,1), (2,-1), (1,-2), (-1,-2)
]

class Solution:
    def shortestPath(self, grid, source, destination):
        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y) : 0}
        while queue:
            x, y = queue.popleft()
            if (x,y) == (destination.x, destination.y):
                return distance[(x,y)]
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue
                distance[(next_x, next_y)] = distance[(x,y)] + 1
                queue.append((next_x,next_y))
        return -1
    
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return not grid[x][y]

# 主函数
if __name__ == '__main__':
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    source = Point(2,0)
    desti = Point(2,2)
    s = Solution()
    print("Input: nums = ", grid, ", source = ",source, ", destination = ", desti)
    print("Output: ", s.shortestPath(grid,source,desti))


# 运行结果
# Input: nums =  [[0, 0, 0], [0, 0, 0], [0, 0, 0]] , source =  [2,0] , destination =  [2,2]
# Output:  2