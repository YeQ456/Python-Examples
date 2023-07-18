# 问题描述
# 给定一个整数数组，将其重新排序，按照排序后的顺序构造最小的数


# 示例
# 输入：[3,32,321]
# 输出：[321,32,3]


# 源码实现
from functools import cmp_to_key
class Solution:
	def cmp(self, a, b):
		if a + b > b + a:
			return 1
		if a + b < b + a:
			return -1
		else:
			return 0

	def PrintMinNumber(self, numbers):
		if not numbers:
			return ""
		number = list(map(str, numbers))
		number.sort(key = cmp_to_key(self.cmp))
		return "".join(number).lstrip('0') or '0'

if __name__ == '__main__':
	generator = [3,32,321]
	s = Solution()
	print("输入：", generator)
	print("输出：", s.PrintMinNumber(generator))


# 运行结果
# 输入： [3, 32, 321]
# 输出： 321323