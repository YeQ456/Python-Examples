# 问题描述
# 给定表示地图坐标的2D数组，地图上只有值0,1,2。 0表示可以通过，1表示不可通过，2表示目标位置。从坐标[0,0]开始，只能上、下、左、右
# 移动，找到可以到达目的地的最短路径，并返回路径的长度


# 示例
# 输入：targetMap
# [
# 	[0,0,0],
# 	[0,0,1],
# 	[0,0,2]
# ]
# 输出：4


# 源码实现
class Solution:
	ans = []
	def cal(self, targetMap, x, y, z):
		if targetMap[x][y] == 1:
			return
		if z < self.ans[x][y] or self.ans[x][y] == -1:
			self.ans[x][y] = z
			if x != 0:
				self.cal(targetMap, x - 1, y, z + 1)
			if x != len(targetMap) - 1:
				self.cal(targetMap, x + 1, y, z + 1)
			if y != 0:
				self.cal(targetMap, x, y - 1, z + 1)
			if y != len(targetMap[0]) - 1:
				self.cal(targetMap, x, y + 1, z + 1)
		return

	def shortestPath(self, targetMap):
		self.ans = [[-1 for i in range(len(targetMap[0]))] for j in range(len(targetMap))]
		self.cal(targetMap, 0, 0, 0)
		# print(self.ans)
		for i in range(len(targetMap)):
			for j in range(len(targetMap[0])):
				if targetMap[i][j] == 2:
					return self.ans[i][j]

if __name__ == '__main__':
	targetMap = [[0,0,0],[0,0,1],[0,0,2]]
	s = Solution()
	print("地图：", targetMap)
	print("最少需要走：", s.shortestPath(targetMap))


# 运行结果
# 地图： [[0, 0, 0], [0, 0, 1], [0, 0, 2]]
# 最少需要走： 4