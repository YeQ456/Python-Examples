# 问题描述
# 给出一个字符串，找到第1个只出现1次的字符


# 示例
# 输入："abaccdeff"
# 输出：b


# 源码实现
class Solution:
	def firstUniqChar(self, str):
		counter = {}
		for c in str:
			counter[c] = counter.get(c, 0) + 1
		for c in str:
			if counter[c] == 1:
				return c

if __name__ == '__main__':
	s = Solution()
	str = "abaccdeff"
	ans = s.firstUniqChar(str)
	print("输入：", str)
	print("输出：", ans)


# 运行结果
# 输入： abaccdeff
# 输出： b