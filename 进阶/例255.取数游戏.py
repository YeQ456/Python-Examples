# 问题描述
# 一个数组arr，由2个玩家1号和2号轮流从数组中取数。只能从数组的两头进行取数，且一次只能取1个。两人都采取最优策略，直到最后数组中的数被
# 取完后，谁取的总和多，就赢得胜利。1号玩家先取，问最后谁将获胜。若1号玩家必胜或两人打成平局，返回1；若2号玩家必胜，返回2‘


# 示例
# 输入：arr = [1,3,1,1]
# 输出：1


# 源码实现
class Solution:
	def theGameOfTakeNumbers(self, arr):
		n = len(arr)
		if n == 0:
			return 1
		sum = [0 for i in range(n)]
		for i in range(1, n + 1):
			for j in range(0, n - i + 1):
				if i == 1:
					sum[j] = arr[j]
					continue
				k = j + i - 1
				sum[j] = max(arr[k] - sum[j], arr[j] - sum[j + 1])
		return 1 if sum[0] >= 0 else 2

if __name__ == '__main__':
	arr = [1,3,3,1]
	s = Solution()
	print("游戏数组：", arr)
	print("赢家：", s.theGameOfTakeNumbers(arr))


# 运行结果
# 游戏数组： [1, 3, 3, 1]
# 赢家： 1