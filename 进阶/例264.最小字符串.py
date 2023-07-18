# 问题描述
# 给定一个长度为n、只包含小写字母的字符串s，从中去掉k个字符，得到一个长度为n ~ k的新字符串。设计算法，输出字典序最小的新字符串


# 示例
# 输入：s = "abccc", k = 2
# 输出："abc"

# 输入：s = "bacdb", k = 2
# 输出："acb"

# 输入：s = "cba", k = 2
# 输出："a"


# 源码实现
class Solution:
	def findMinC(self, s, k):
		ans = 0
		if len(s) <= k:
			return -1
		for i in range(1, k + 1):
			if ord(s[i]) < ord(s[i - 1]):
				ans = i
		return ans

	def MinimumString(self, s, k):
		ans = ""
		while k > 0:
			temp = self.findMinC(s, k)
			if temp == -1:
				s = ''
				break
			ans = ans + s[temp]
			s = s[temp + 1:]
			k -= temp
		ans += s
		return ans

if __name__ == '__main__':
	s = "cba"
	k = 2
	ss = Solution()
	print("原始字符串：", s)
	print("可删除后最小字典序：", ss.MinimumString(s, k))


# 运行结果
# 原始字符串： cba
# 可删除后最小字典序： a