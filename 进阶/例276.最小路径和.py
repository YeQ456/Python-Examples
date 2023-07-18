# 问题描述
# 给定一个只含非负整数m X n网格，找到一条从左上角到右下角的路径，使数字和最小，返回路径和


# 示例
# 输入：[[1,3,1],[1,5,1],[4,2,1]]
# 输出：7


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

if __name__ == '__main__':
	s = Solution()
	nums = [[1,3,1],[1,5,1],[4,2,1]]
	ans = s.minPathSum(nums)
	print("输入列表：", nums)
	print("输出路径和：", ans)


# 运行结果
# 输入列表： [[1, 4, 5], [2, 7, 6], [6, 8, 7]]
# 输出路径和： 7