# 问题描述
# 在一篇文章中，一个短语由至少k个连续的单词组成，且其总长度不小于lim。将一篇文章以一个字符串数组str的形式给出，输出的文章中
# 最短的短语长度


# 示例
# 输入：k = 2, lim = 7, str = ["i","love","longterm","so","much"]
# 输出：10

# 输入：k = 2, lim = 10, str = ["she","was","bad","in","singing"]
# 输出：11


# 源码实现
class Solution:
	def getLength(self, k, lim, str):
		n = len(str)
		arr = [0] * n
		for i in range(n):
			arr[i] = len(str[i])
		l = 0
		r = 0
		sum = 0
		ans = 1e9
		for r in range(n):
			sum += arr[r]
			while r - l >= k and sum - arr[l] > lim:
				sum -= arr[l]
				l += 1
			if r - l + 1 >= k and sum >= lim:
				ans = min(ans, sum)
		return ans

if __name__ == '__main__':
	k = 2
	lim = 10
	str = ["she","was","bad","in","singing"]
	s = Solution()
	print("最短单词数：", k)
	print("短语长度限制为大于：", lim)
	print("文章列表：", str)
	print("最短短语：", s.getLength(k, lim, str))


# 运行结果
# 最短单词数： 2
# 短语长度限制为大于： 10
# 文章列表： ['she', 'was', 'bad', 'in', 'singing']
# 最短短语： 11