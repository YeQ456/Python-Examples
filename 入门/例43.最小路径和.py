# 问题描述
# 给定一个只含非负整数的m * n网络，寻找一条从左上角到右下角的路径，使数字和最小


# 示例
# 输入：[[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：1 -> 3 -> 1 -> 1 -> 1

# 输入：[[1,3,2]]
# 输出：6
# 解释：1 -> 3 -> 2


# 源码实现
class Solution:
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[len(grid) - 1][len(grid[0]) - 1]

# 主函数
if __name__ == '__main__':
    solution = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    length = solution.minPathSum(grid)
    print("Input: grid = ", grid)
    print("Output: ", length)



# 运行结果
# Input: grid =  [[1, 4, 5], [2, 7, 6], [6, 8, 7]]
# Output: 7