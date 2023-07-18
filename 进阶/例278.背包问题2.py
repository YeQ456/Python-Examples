# 问题描述
# 给出n个物品的体积A[i]和其价值V[i]，将它们装入一个大小为m的背包，求能装入的最大总价值


# 示例
# 输入：物品体积[2,3,5,7], 对应价值[1,5,2,4], 背包大小：10
# 输出：最大总价值为9


# 源码实现
class Solution:
	def backPackII(self, m, A, V):
		n = len(A)
		dp = [[0] * (m + 1), [0] * (m + 1)]
		for i in range(1, n + 1):
			dp[i % 2][0] = 0
			for j in range(1, m + 1):
				dp[i % 2][j] = dp[(i - 1) % 2][j]
				if A[i - 1] <= j:
					dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - A[i - 1]] + V[i - 1])
		return dp[n % 2][m]


if __name__ == '__main__':
	s = Solution()
	vol = 34
	nums = [4,13,2,6,7,11,8]
	val = [1,23,4,5,2,14,9]
	ans = s.backPackII(vol, nums, val)
	print("输入总体积：", vol)
	print("输入物品：", nums)
	print("输入价值：", val)
	print("输出结果：", ans)


# 运行结果
# 输入总体积： 34
# 输入物品： [4, 13, 2, 6, 7, 11, 8]
# 输入价值： [1, 23, 4, 5, 2, 14, 9]
# 输出结果： 50