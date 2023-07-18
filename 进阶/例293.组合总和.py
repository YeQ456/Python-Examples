# 问题描述
# 给出一个都是正整数的数组nums，其中没有重复的数，找出所有和为target的组合个数


# 示例
# 输入：nums = [1,2,4], target = 4
# 输出：6


# 源码实现
class Solution:
	def backPackVI(self, nums, target):
		row = len(nums)
		col = target
		dp = [0 for i in range(col + 1)]
		dp[0] = 1
		for j in range(1, col + 1):
			for i in range(1, row + 1):
				if nums[i - 1] > j:
					continue
				dp[j] += dp[j - nums[i - 1]]
		return dp[-1]

if __name__ == '__main__':
	generator = [1,2,4]
	target = 4
	s = Solution()
	print("输入：", generator)
	print("输出：", s.backPackVI(generator, target))


# 运行结果
# 输入： [1, 2, 4]
# 输出： 6