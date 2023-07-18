# 问题描述
# 给出字符串，选择在1个字符或2个相邻字符之后拆分字符串，使字符串仅由1个字符或2个字符组成，输出所有可能的结果


# 示例
# 输入："123"
# 输出：[["1","2","3"],["12","3"],["1","23"]]

# 输入："12345"
# 输出：[["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],
#        ["12","3","4","5"],["1","2","3","4","5"]]


# 源码实现
class Solution:
	def splitString(self, s):
		result = []
		self.dfs(result, [], s)
		return result

	def dfs(self, result, path, s):
		if s == "":
			result.append(path[:])
			return
		for i in range(2):
			if i + 1 <= len(s):
				path.append(s[:i + 1])
				self.dfs(result, path, s[i + 1:])
				path.pop()

if __name__ == '__main__':
	s = Solution()
	ss = "123"
	ans = s.splitString(ss)
	print("输入：", ss)
	print("输出：", ans)


# 运行结果
# 输入： 123
# 输出： [['1', '2', '3'], ['1', '23'], ['12', '3']]