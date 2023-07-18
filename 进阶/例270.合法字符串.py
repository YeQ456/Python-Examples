# 问题描述
# 给定一个只包含大写字母的字符串S，在S中插入尽量少的字符"_"，使同一种字母间隔至少为k。若有多种插入方式，则选择目标字符串字典序
# 最小的方式


# 示例
# 输入：S = "AABACCDCD", k = 3
# 输出：[0,2,0,1,0,2,0,1,0]

# 输入：S = "ABBA", k = 2
# 输出：[0,0,1,0]


# 源码实现
class Solution:
	def getAns(self, k, s):
		n = len(S)
		pre = [-1] * 26
		sm = [0] * (n + 1)
		ans = []
		for i in range(1, n + 1):
			c = ord(S[i - 1]) - ord('A')
			if pre[c] == -1 or sm[i - 1] - sm[pre[c]] - pre[c] + i >= k:
				sm[i] = sm[i - 1]
				ans.append(0)
			else:
				sm[i] = sm[i - 1] + k - (sm[i - 1] - sm[pre[c]] + i - pre[c])
				ans.append(k - (sm[i - 1] - sm[pre[c]] + i - pre[c]))
			pre[c] = i
		return ans

if __name__ == '__main__':
	S = "AABACCDCD"
	k = 3
	s = Solution()
	print("字符串",S,"每个相同字符间隔至少",k,"个字符")
	print("_字符的列表：", s.getAns(k,S))


# 运行结果
# 字符串 AABACCDCD 每个相同字符间隔至少 3 个字符
# _字符的列表： [0, 2, 0, 1, 0, 2, 0, 1, 0]