# 问题描述
# 一串技能必须按照顺序释放，释放顺序为arr。每个技能都有长度为n的冷却时间，且两个同类技能之间至少要间隔n秒。释放每个技能需要1秒，返回放完
# 所有技能所需要的时间


# 示例
# 输入：arr = [1,1,2,2], n = 2
# 输出：8

# 输入：arr = [1,2,1,2], n = 2
# 输出：5


# 源码实现
class Solution:
	def askForCoolingTime(self, arr, n):
		ans = 0
		l = [0 for i in range(110)]
		for x in arr:
			if l[x] == 0 or ans - l[x] > n:
				ans += 1
			else:
				ans = l[x] + n + 1
			l[x] = ans
		return ans

if __name__ == '__main__':
	arr = [1,2,1,2]
	n = 2
	s = Solution()
	print("数组：", arr, " 冷却时间：", n)
	print("至少需要时间：", s.askForCoolingTime(arr, n))


# 运行结果
# 数组： [1, 2, 1, 2]  冷却时间： 2
# 至少需要时间： 5