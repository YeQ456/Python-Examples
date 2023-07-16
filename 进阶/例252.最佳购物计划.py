# 问题描述
# 假设你有k元，商场里有n个礼盒，m个商品，每个商品和礼盒都有一个对应的价值val[i]和费用cost[i]，对于每个商品，只有在购买了其对应的礼盒belong[i]后才能购买
# 给出n、m大小为n+m的数组val、cost和belong，在花费不超过k的情况下得到的商品和礼盒的最大价值为多少？


# 示例
# 输入：n=3,m=2,k=10,val=[17,20,8,1,4],cost=[3,5,2,3,1],belong=[-1,-1,-1,0,2]
# 输出：45

# 输入：n=2,m=4,k=9,val=[5,7,7,18,16,8],cost=[1,1,3,3,3,5],belong=[-1,-1,1,0,1,1]
# 输出：46

# 输入：n=2,m=2,k=10,val=[10,1,20,20],cost=[1,10,2,3],belong=[-1,-1,0,0]
# 输出：50


# 源码实现
class Solution:
	def getAns(self, n, m, k, val, cost, belong):
		dp = [[-1 for i in range(0, 100001)] for i in range(0, 105)]
		arr = [[] for i in range(0, 105)]
		for i in range(n, n + m):
			if not belong[i] == -1:
				arr[belong[i]].append(i)
		dp[0][cost[0]] = val[0]
		for i in arr[0]:
			for j in range(k, cost[i] - 1, -1):
				if not dp[0][j - cost[i]] == -1:
					dp[0][j] = dp[0][j - cost[i]] + val[i]
		for i in range(1, n):
			for j in range(k, cost[i] - 1, -1):
				if not dp[i - 1][j - cost[i]] == -1:
					dp[i][j] = dp[i - 1][j - cost[i]] + val[i]
			dp[i][cost[i]] = val[i]
			for j in arr[i]:
				for l in range(k, cost[j] - 1, -1):
					if not dp[i][l - cost[j]] == -1:
						dp[i][l] = max(dp[i][l], dp[i][l - cost[j]] + val[j])
			for j in range(0, k + 1):
				dp[i][j] = max(dp[i][j], dp[i - 1][j])
		ans = 0
		for i in range(0, k + 1):
			ans = max(ans, dp[n - 1][i])
		return ans

if __name__ == '__main__':
	k = 10
	m = 2
	n = 3
	val = [17,20,8,1,4]
	cost = [3,5,2,3,1]
	belong = [-1,-1,-1,0,2]
	s = Solution()
	print("拥有的钱：", k)
	print("商品数：", m, " 礼盒数：", n)
	print("价值列表：", val, " 费用列表：", cost)
	print("得到最大价值：", s.getAns(n,m,k,val,cost,belong))


# 运行结果
# 拥有的钱： 10
# 商品数： 2  礼盒数： 3
# 价值列表： [17, 20, 8, 1, 4]  费用列表： [3, 5, 2, 3, 1]
# 得到最大价值： 45