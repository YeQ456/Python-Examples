# 问题描述
# 给定一个数n，生成一个包含1 ~ n²的顺时针螺旋形矩阵


# 示例
# 输入：2
# 输出：
# [[1,2],
#  [4,3]
# ]

# 输入：3
# 输出：
# [[1,2,3],
#  [8,9,4],
#  [7,6,5]
# ]


# 源码实现
class Solution:
	def generateMatrix(self, n):
		if n == 0:
			return []
		matrix = [[0 for i in range(n)] for j in range(n)]
		up = 0
		down = len(matrix) - 1
		left = 0
		right = len(matrix[0]) - 1
		direct = 0
		count = 0
		while True:
			if direct == 0:
				for i in range(left, right + 1):
					count += 1
					matrix[up][i] = count
				up += 1
			if direct == 1:
				for i in range(up, down + 1):
					count += 1
					matrix[i][right] = count
				right -= 1
			if direct == 2:
				for i in range(right, left - 1, -1):
					count += 1
					matrix[down][i] = count
				down -= 1
			if direct == 3:
				for i in range(down, up - 1, -1):
					count += 1
					matrix[i][left] = count
				left += 1
			if count == n * n:
				return matrix
			direct = (direct + 1) % 4

if __name__ == '__main__':
	n = 3
	s = Solution()
	print("输入：n = ", n)
	print("输出：", s.generateMatrix(n))


# 运行结果
# 输入：n =  3
# 输出： [[1, 2, 3], [8, 9, 4], [7, 6, 5]]