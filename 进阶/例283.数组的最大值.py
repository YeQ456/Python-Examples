# 问题描述
# 给定一个浮点数数组，求数组中的最大值


# 示例
# 输入：[1.0,2.1,-3.3]
# 输出：2.1


# 源码实现
class Solution:
	def max_num(self, arr):
		if arr == []:
			return
		maxmum = arr[0]
		for x in arr:
			if x > maxmum:
				maxmum = x
		return maxmum

if __name__ == '__main__':
	s = Solution()
	arr = [1.0,2.1,-3.3]
	ans = s.max_num(arr)
	print("输入：", arr)
	print("输出：", ans)


# 运行结果
# 输入： [1.0, 2.1, -3.3]
# 输出： 2.1