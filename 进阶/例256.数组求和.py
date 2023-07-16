# 问题描述
# 给定一个数组arr, 分别对其每个子数组求和，再把所有的和加起来，返回加起来的值。并且返回的值对1000000007取模


# 示例
# 输入：arr = [2,4,6,8,10]
# 输出：210


# 源码实现
class Solution:
	def findTheSumOfTheArray(self, arr):
		ans = 0
		n = len(arr)
		for i in range(n):
			ans = (ans + arr[i] * (i + 1) * (n - i)) % 1000000007
		return ans

if __name__ == '__main__':
	arr = [2,4,6,8,10]
	s = Solution()
	print("输入数组：", arr)
	print("所有子数组的和：", s.findTheSumOfTheArray(arr))


# 运行结果
# 输入数组： [2, 4, 6, 8, 10]
# 所有子数组的和： 210