# 问题描述
# 给出布尔型二维数组，0表示海，1表示岛屿。若两个1相邻，则认为是同一个岛屿，只考虑上下左右相邻，找到大小在k及k以上岛屿的数量


# 示例
# 输入二维数组：
# [
# 	[1,1,0,0,0],
# 	[0,1,0,0,1],
# 	[0,0,0,1,1],
# 	[0,0,0,0,0],
# 	[0,0,0,0,1]
# ]
# 输入k = 3
# 输出：2


# 源码实现
class Solution:
	def numsofIsland(self, grid, k):
		if not grid or len(grid) == 0 or len(grid[0]) == 0:
			return 0
		rows, cols = len(grid), len(grid[0])
		visited = [[False for i in range(cols)] for i in range(rows)]
		res = 0
		for i in range(rows):
			for j in range(cols):
				if visited[i][j] == False and grid[i][j] == 1:
					check = self.bfs(grid, visited, i, j, k)
					if check:
						res += 1
		return res

	def bfs(self, grid, visited, x, y, k):
		rows, cols = len(grid), len(grid[0])
		import collections
		queue = collections.deque([(x, y)])
		visited[x][y] = True
		res = 0
		while queue:
			item = queue.popleft()
			res += 1
			for idx, idy in ((1,0),(-1,0),(0,1),(0,-1)):
				x_new, y_new = item[0] + idx, item[1] + idy
				if x_new < 0 or x_new >= rows or y_new < 0 or y_new >= cols \
				   or visited[x_new][y_new] or grid[x_new][y_new] == 0:
				   continue
				queue.append((x_new, y_new))
				visited[x_new][y_new] = True
		return res >= k

if __name__ == "__main__":
	s = Solution()
	g = [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]
	k = 3
	ans = s.numsofIsland(g, k)
	print("输入：", g, "\nk = ", k)
	print("输出：", ans)


# 运行结果
# 输入： [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]] 
# k =  3
# 输出： 2