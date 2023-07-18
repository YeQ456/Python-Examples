# 问题描述
# 每个人都有自己的网上好友。现在有n个人，给出m对好友关系，问任意一个人是否能直接或间接联系到网上所有的人。若能，返回YES；若
# 不能，返回NO。好友关系用a数组和b数组表示，代表a[i]和b[i]是一对好友


# 示例
# 输入：n = 4, a = [1,1,1], b = [2,3,4]
# 输出：YES

# 输入：n = 5, a = [1,2,4], b = [2,3,5]
# 输出：NO


# 源码实现
class Solution:
	father = [0] * 5000
	def ask(self, x):
		if Solution.father[x] == x:
			return x
		Solution.father[x] = Solution.ask(self, Solution.father[x])
		return Solution.father[x]

	def socialNetwork(self, n, a, b):
		for i in range(0, n):
			Solution.father[i] = i
		m = len(b)
		for i in range(m):
			x = Solution.ask(self, a[i])
			y = Solution.ask(self, b[i])
			Solution.father[x] = y
		for i in range(0, n):
			if Solution.ask(self, i) != Solution.ask(self, 1):
				return "NO"
		return "YES"

if __name__ == '__main__':
	n = 4
	a = [1,1,1]
	b = [2,3,4]
	s = Solution()
	print("好友关系组：", a, b)
	print("他们能否直接或间接互相联系：", s.socialNetwork(n, a, b))


# 运行结果
# 好友关系组： [1, 1, 1] [2, 3, 4]
# 他们能否直接或间接互相联系： YES