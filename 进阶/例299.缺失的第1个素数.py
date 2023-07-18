# 问题描述
# 给出一个素数数组，找到最小未出现的素数


# 示例
# 输入：[3,5,7]
# 输出：2

# 输入：[2,3,5,7,11,13,17,23,29]
# 输出：19


# 源码实现
class Solution:
	def firstMissPrime(self, nums):
		if not nums:
			return 2
		start = 0
		l = len(nums)
		integer = 2
		while start < l:
			while self.isPrime(integer) == False:
				integer += 1
			if nums[start] != integer:
				return integer
			integer += 1
			start += 1
		while self.isPrime(integer) == False:
			integer += 1
		return integer

	def isPrime(self, num):
		if num == 2 or num == 3:
			return True
		for i in range(2, int(num ** (0.5)) + 1):
			if num % i == 0:
				return False
		return True

if __name__ == '__main__':
	s = Solution()
	n = [3,5,7]
	print("输入：", n)
	print("输出：", s.firstMissPrime(n))


# 运行结果
# 输入： [3, 5, 7]
# 输出： 2