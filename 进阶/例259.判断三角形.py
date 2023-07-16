# 问题描述
# 给定一个数组arr，判断能否从数组里找到3个元素作为3条边的边长，使3条边能够组成一个三角形。若能，返回YES，否则返回NO


# 示例
# 输入：arr = [2,3,5,8]
# 输出：NO

# 输入：arr = [3,4,5,8]
# 输出：YES


# 源码实现
class Solution:
	def judgingTriangle(self, arr):
		n = len(arr)
		if n > 44:
			return "YES"
		arr.sort()
		for i in range(n - 2):
			for j in range(i + 1, n - 1):
				for k in range(j + 1, n):
					if arr[i] + arr[j] > arr[k]:
						return "YES"
		return "NO"

if __name__ == '__main__':
	a = [1,2,5,9,10]
	s = Solution()
	print("输入数组：", a)
	print("能否组成三角形：", s.judgingTriangle(a))


# 运行结果
# 输入数组： [1, 2, 5, 9, 10]
# 能否组成三角形： YES