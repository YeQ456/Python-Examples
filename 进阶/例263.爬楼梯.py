# 问题描述
# 准备爬n个台阶的楼梯，当位于第i级台阶时，可以往上走1至num[i]级台阶。问有多少种爬完楼梯的方法，返回的答案对10^9 + 7取模


# 示例
# 输入：n = 3, num = [3,2,1]
#输出：4


# 源码实现
class Solution:
	def getAnswer(self, n, num):
		ans = [0] * (len(num) + 1)
		ans[0] = 1
		for i in range(n):
			for j in range(1 + i, min(len(num) + 1, i + num[i] + 1)):
				ans[j] = (ans[j] + ans[i]) % (10 ** 9 + 7)
		return ans[len(num)]

if __name__ == '__main__':
	n = 4
	num = [1,1,1,1]
	s = Solution()
	print("台阶数和每层台阶能往上登的阶数：", n, num)
	print("走到顶一共有：", s.getAnswer(n, num), "种走法")


# 运行结果
# 台阶数和每层台阶能往上登的阶数： 4 [1, 1, 1, 1]
# 走到顶一共有： 1 种走法