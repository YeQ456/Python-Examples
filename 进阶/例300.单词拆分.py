# 问题描述
# 给出一个单词表和一条去掉所有空格的句子，根据给出的单词表添加空格，返回可以构成句子的数量。保证构成句子的单词都能在单词表中找到


# 示例
# 输入："CatMat", 单词表：["Cat","Mat","Ca","tM","at","C","Dog","og","Do"]
# 输出：3


# 源码实现
class Solution:
	def wordBreak(self, s, dict):
		if not s or not dict:
			return 0
		n, hash = len(s), set()
		lowerS = s.lower()
		for d in dict:
			hash.add(d.lower())
		f = [[0] * n for _ in range(n)]
		for i in range(n):
			for j in range(i, n):
				sub = lowerS[i:j + 1]
				if sub in hash:
					f[i][j] = 1
		for i in range(n):
			for j in range(i, n):
				for k in range(i, j):
					f[i][j] += f[i][k] * f[k + 1][j]
		return f[0][-1]

if __name__ == '__main__':
	s = Solution()
	str = "CatMat"
	dict = ["Cat","Mat","Ca","tM","at","C","Dog","og","Do"]
	print("输入句子：", str)
	print("输入列表：", dict)
	print("输出数量：", s.wordBreak(str, dict))


# 运行结果
# 输入句子： CatMat
# 输入列表： ['Cat', 'Mat', 'Ca', 'tM', 'at', 'C', 'Dog', 'og', 'Do']
# 输出数量： 3