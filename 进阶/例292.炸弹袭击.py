# 问题描述
# 给定一个二维矩阵，每一个格子可能是一堵墙W、一个敌人E或者空气0。返回用一个炸弹可杀死的最多敌人数。炸弹会杀死所有在同一行和同一列
# 没有墙阻隔的敌人。墙不会被摧毁，只能在空地放置炸弹


# 示例
# 输入：
# grid = [
# 	"0E00",
# 	"E0WE",
# 	"0E00"
# ]
# 输出：3


# 源码实现
class Solution:
	def maxKillEnemies(self, grid):
		m, n = len(grid), 0
		if m:
			n = len(grid[0])
		result, rows = 0, 0
		cols = [0 for i in range(n)]
		for i in range(m):
			for j in range(n):
				if j == 0 or grid[i][j - 1] == 'W':
					rows = 0
					for k in range(j, n):
						if grid[i][k] == 'W':
							break
						if grid[i][k] == 'E':
							rows += 1
				if i == 0 or grid[i - 1][j] == 'W':
					cols[j] = 0
					for k in range(i, m):
						if grid[k][j] == 'W':
							break
						if grid[k][j] == 'E':
							cols[j] += 1
				if grid[i][j] == '0' and rows + cols[j] > result:
					result = rows + cols[j]
		return result

if __name__ == '__main__':
	generator = [
		"0E00",
 		"E0WE",
 		"0E00"
 		]
	s = Solution()
	print("输入：", generator)
	print("输出：", s.maxKillEnemies(generator))


# 运行结果
# 输入： ['0E00', 'E0WE', '0E00']
# 输出： 3