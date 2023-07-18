# 问题描述
# 设计一种方法，通过给重复字符计数来进行基本的字符串压缩。字符串"aabcccccaaa"可压缩为"a2b1c5a3"。若压缩后的字符数不小于原始的
# 字符数，则返回原始的字符串。（假设字符串只包含a ~ z字母）


# 示例
# 输入：str = "aabcccccaaa"
# 输出："a2b1c5a3"

# 输入：str = "aabbcc"
# 输出："aabbcc"


# 源码实现
class Solution:
	def compress(self, originalString):
		l = len(originalString)
		if l <= 2:
			return originalString
		length = 1
		res = ""
		for i in range(1,l):
			if originalString[i] != originalString[i - 1]:
				res = res + originalString[i - 1] + str(length)
				length = 1
			else:
				length += 1
		if originalString[-1] != originalString[-2]:
			res = res + originalString[-1] + "1"
		else:
			res = res + originalString[i - 1] + str(length)
		if len(originalString) <= len(res):
			return originalString
		else:
			return res

if __name__ == '__main__':
	s = Solution()
	si = "aabcccccaaa"
	arr = list(si)
	ans = s.compress(arr)
	print("输入：", si)
	print("输出：", ans)


# 运行结果
# 输入： aabcccccaaa
# 输出： a2b1c5a3