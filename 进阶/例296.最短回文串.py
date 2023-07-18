# 问题描述
# 给定一个字符串S，可以通过在前面添加字符转换为回文串，返回用这种方式转换的最短回文串


# 示例
# 输入："aacecaaa"
# 输出："aaacecaaa"


# 源码实现
class Solution:
	def convertPalindrome(self, str):
		if not str or len(str) == 0:
			return ""
		n = len(str)
		for i in range(n - 1, -1, -1):
			substr = str[:i + 1]
			if self.isPalindrome(substr):
				if i == n - 1:
					return str
				else:
					return (str[i + 1:][::-1]) + str[:]

	def isPalindrome(self, str):
		left, right = 0, len(str) - 1
		while left < right:
			if str[left] != str[right]:
				return False
			left += 1
			right -= 1
		return True

if __name__ == "__main__":
	s = Solution()
	ss = "sdsdlkjsaoio"
	ans = s.convertPalindrome(ss)
	print("输入：", ss)
	print("输出：", ans)


# 运行结果
# 输入： sdsdlkjsaoio
# 输出： oioasjkldsdsdlkjsaoio