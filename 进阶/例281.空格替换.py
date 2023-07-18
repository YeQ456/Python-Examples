# 问题描述
# 设计一种方法，将一个字符串中所有空格替换成%20(假设该字符串有足够的空间加入新的字符)。返回被替换后的字符串长度


# 示例
# 输入：string[] = "Mr John Smith", length = 13
# 输出：string[] = "Mr%20John%20Smith", length = 17


# 源码实现
class Solution:
	def replaceBlank(self, string, length):
		if string is None:
			return length
		f = 0
		L = len(string)
		for i in range(len(string)):
			if string[i] == ' ':
				string[i] = '%20'
				f += 1
		return L - f + f * 3

if __name__ == '__main__':
	s = Solution()
	si = "Mr John Smith"
	s1 = list(si)
	ans = s.replaceBlank(s1, 13)
	so = ''.join(s1)
	print("输入字符串：", si)
	print("输出字符串：", so)
	print("长度：", ans)


# 运行结果
# 输入字符串： Mr John Smith
# 输出字符串： Mr%20John%20Smith
# 长度： 17