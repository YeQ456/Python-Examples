# 问题描述
# 给定一个整数数组，在该数组中寻找3个数，分别代表三角形3条边的长度。可以寻找多少组这样的3个数来组成三角形？


# 示例
# 输入：[3,4,6,7]
# 输出：3


# 源码实现
class Solution:
	def triangleCount(self, S):
		if len(S) < 3:
			return
		count = 0
		S.sort()
		for i in range(0, len(S)):
			for j in range(i + 1, len(S)):
				w, r = i + 1, j
				target = S[j] - S[i]
				while w < r:
					mid = (w + r) // 2
					S_mid = S[mid]
					if S_mid > target:
						r = mid
					else:
						w = mid + 1
				count += (j - w)
		return count

if __name__ == '__main__':
	generator = [3,4,6,7]
	s = Solution()
	print("输入：", generator)
	print("输出：", s.triangleCount(generator))


# 运行结果
# 输入： [3, 4, 6, 7]
# 输出： 3