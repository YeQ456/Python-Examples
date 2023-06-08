# 问题描述
# 给定二维矩阵，计算由左上角坐标(row1, col1)和右下角坐标(row2, col2)划定的矩阵内元素的和。假设矩阵
# 不变，row1 <= row2 并且 col1 <= col2


# 示例
# 输入：[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]], sumRegion(2,1,4,3)
# sumRegion(1,1,2,2), sumRegion(1,2,2,4)
# 输出：8,11,12
# 解释：
# 根据给出的矩阵：
# [
#   [3,0,1,4,2],
#   [5,6,3,2,1],
#   [1,2,0,1,5],
#   [4,1,0,1,7],
#   [1,0,3,0,5]
# ]
# sumRegion(2,1,4,3) = 2 + 0 + 1 + 1 + 0 + 1 + 0 + 3 + 0 = 8
# sumRegion(1,1,2,2) = 6 + 3 + 2 + 0 = 11
# sumRegion(1,2,2,4) = 3 + 2 + 1 + 0 + 1 + 5 = 12

# 输入：[[3,0],[5,6]], sumRegion(0,0,0,1), sumRegion(0,0,1,1)
# 输出：3,14
# 给出矩阵：
# [
#   [3,0],
#   [5,6]
# ]
# sumRegion(0,0,0,1) = 3 + 0 = 3
# sumRegion(0,0,1,1) = 3 + 0 + 5 + 6 = 14


# 源码实现
class NumMatrix(object):
    def __init__(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        n = len(matrix)
        m = len(matrix[0])
        self.dp = [[0] * (m + 1) for _ in range(n + 1)]
        for r in range(n):
            for c in range(m):
                self.dp[r + 1][c + 1] = self.dp[r + 1][c] + self.dp[r][c + 1] + \
                    matrix[r][c] - self.dp[r][c]
    
    def sumRegion(self, row1, col1, row2, col2):
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - \
            self.dp[row2 + 1][col1] + self.dp[row1][col1]

# 主函数
if __name__ == '__main__':
    nums = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
    s = NumMatrix(nums)
    print("输入矩阵：", nums)
    print("区域1的和：", s.sumRegion(2,1,4,3))
    print("区域2的和：", s.sumRegion(1,1,2,2))
    print("区域3的和：", s.sumRegion(1,2,2,4))


# 运行结果
# 输入矩阵：[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
# 区域1的和：8
# 区域2的和：11
# 区域3的和：12