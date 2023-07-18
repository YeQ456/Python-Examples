# 问题描述
# 给定数组prices，其中第i个元素代表某只股票在第i天的价格，最多可以完成k笔交易，问最大的利润是多少？


# 示例
# 输入：k = 2, prices = [4,4,6,1,1,4,2,5]
# 输出：6


# 源码实现
class Solution:
	def maxProfit(self, k, prices):
		size = len(prices)
		if k >= size / 2:
			return self.quickSolve(size, prices)
		dp = [-10000] * (2 * k + 1)
		dp[0] = 0
		for i in range(size):
			for j in range(min(2 * k, i + 1), 0, -1):
				dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1,-1][j % 2])
		return max(dp)

	def quickSolve(self, size, prices):
		sum = 0
		for x in range(size - 1):
			if prices[x + 1] > prices[x]:
				sum += prices[x + 1] - prices[x]
		return sum

if __name__ == '__main__':
	s = Solution()
	price = [4,4,6,1,1,4,2,5]
	k = 2
	maxprofit = s.maxProfit(k, price)
	print("输入价格：", price)
	print("交易次数：", k)
	print("最大利润：", maxprofit)


# 运行结果
# 输入价格： [4, 4, 6, 1, 1, 4, 2, 5]
# 交易次数： 2
# 最大利润： 6