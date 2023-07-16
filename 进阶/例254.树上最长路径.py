# 问题描述
# 由n个节点、n-1条边组成的一棵树。求这棵树中距离最远的两个节点之间的距离。给出3个大小为n-1的数组[starts, ends, lens]表示
# 第i条边是从starts[i]连向ends[i]，长度为lens[i]的无向边


# 示例
# 输入：n = 5, starts = [0,0,2,2], ends = [1,2,3,4], lens = [1,2,5,6]
# 输出：11

# 输入：n = 5, starts = [0,0,2,2], ends = [1,2,3,4], lens = [5,2,5,6]
# 输出：13


# 源码实现
import sys
sys.setrecursionlimit(200000)
class Solution:
	G = []
	dp = []
	def dfs(self, u, pre):
		for x in self.G[u]:
			if x[0] != pre:
				self.dp[x[0]] = self.dp[u] + x[1]
				self.dfs(x[0], u)

	def longestPath(self, n, starts, ends, lens):
		self.G = [[] for i in range(n)]
		self.dp = [0 for i in range(n)]
		for i in range(n - 1):
			self.G[starts[i]].append([ends[i], lens[i]])
			self.G[ends[i]].append([starts[i], lens[i]])
		self.dp[0] = 0
		self.dfs(0, 0)
		pos = Mx = 0
		for i in range(n):
			if self.dp[i] > Mx:
				pos = i
				Mx = self.dp[i]
		self.dp[pos] = 0
		self.dfs(pos, pos)
		ans = 0
		for i in range(n):
			if self.dp[i] > ans:
				ans = self.dp[i]
		return ans

if __name__ == '__main__':
	n = 5
	starts = [0,0,2,2]
	ends = [1,2,3,4]
	lens = [1,2,5,6]
	s = Solution()
	print("总节点数：", n)
	print("每条边的起始：", starts)
	print("每条边的结束：", ends)
	print("每条边的权重：", lens)
	print("树上最长路径：", s.longestPath(n, starts, ends, lens))


# 运行结果
# 总节点数： 5
# 每条边的起始： [0, 0, 2, 2]
# 每条边的结束： [1, 2, 3, 4]
# 每条边的权重： [1, 2, 5, 6]
# 树上最长路径： 11