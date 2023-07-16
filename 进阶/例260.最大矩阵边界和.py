# 问题描述
# 给定一个大小为n X m的矩阵arr, 从arr中找出一个非空子矩阵，使位于这个子矩阵边界上的元素之和最大，输出该子矩阵边界上的元素之和


# 示例
# 输入：arr = [[-1,-3,2],[2,3,4],[-3,7,2]]
# 输出：16

# 输入：arr = [[-1,-1],[-1,-1]]
# 输出：-1

# 输入：arr = [[1,1,1],[1,2,1],[1,1,1]]
# 输出：8


# 源码实现
class Solution:
	def solve(self, arr):
		n = len(arr)
		m = len(arr[0])
		preCol = []
		preRow = []
		for r in range(n):
			tem = [0]
			res = 0
			for c in range(m):
				res += arr[r][c]
				tem.append(res)
			preRow.append(tem)
		for c in range(m):
			tem = [0]
			res = 0
			for r in range(n):
				res += arr[r][c]
				tem.append(res)
			preCol.append(tem)
		ans = arr[0][0]
		for r1 in range(n):
			for r2 in range(r1, n):
				for c1 in range(m):
					for c2 in range(c1, m):
						if r1 == r2 and c1 == c2:
							res = arr[r1][c1]
						elif r1 == r2:
							res = preRow[r1][c2 + 1] - preRow[r1][c1]
						elif c1 == c2:
							res = preCol[c1][r2 + 1] - preCol[c1][r1]
						else:
							res = preCol[c1][r2 + 1] - preCol[c1][r1] + preCol[c2][r2 + 1] - preCol[c2][r1] + \
								  preRow[r1][c2 + 1] - preRow[r1][c1] + preRow[r2][c2 + 1] - preRow[r2][c1] - \
								  arr[r1][c1] - arr[r1][c2] - arr[r2][c1] - arr[r2][c2]
						ans = max(ans, res)
		return ans

if __name__ == '__main__':
	arr = [[-1,-3,2],[2,3,4],[-3,7,2]]
	s = Solution()
	print("矩阵：", arr)
	print("最大能得到边界和：", s.solve(arr))


# 运行结果
# 矩阵： [[-1, -3, 2], [2, 3, 4], [-3, 7, 2]]
# 最大能得到边界和： 16