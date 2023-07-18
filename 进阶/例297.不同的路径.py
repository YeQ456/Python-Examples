# 问题描述
# 给定整数矩阵，起点为左上角元素，终点为右下角元素。只能上下左右移动，给出有权值的地图，找到所有权值不同的路径之和


# 示例
# 输入矩阵：
# [
# 	[1,1,2],
# 	[1,2,3],
# 	[3,2,4]
# ]
# 输出：21


# 源码实现
class Solution:
	def uniqueWeightPaths(self, grid):
		n = len(grid)
		m = len(grid[0])
		if n == 0 or m == 0:
			return 0
		s = [[set() for _ in range(m)] for __ in range(n)]
		s[0][0].add(grid[0][0])
		for i in range(n):
			for j in range(m):
				if i == 0 and j == 0:
					s[i][j].add(grid[i][j])
				else:
					for val in s[i - 1][j]:
						s[i][j].add(val + grid[i][j])
					for val in s[i][j - 1]:
						s[i][j].add(val + grid[i][j])
		ans = 0
		for val in s[-1][-1]:
			ans += val
		return ans

if __name__ == '__main__':
	s = Solution()
	arr = [[1,1,2],[1,2,3],[3,2,4]]
	ans = s.uniqueWeightPaths(arr)
	print("输入：", arr)
	print("输出：", ans)


# 运行结果
# 输入： [[1, 1, 2], [1, 2, 3], [3, 2, 4]]
# 输出： 21