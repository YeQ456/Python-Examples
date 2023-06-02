# 问题描述
# 给出只有0和1组成的二维矩阵，找出最大的一个子矩阵，使得这个矩阵对角线上全为1，其他位置全为0，输出元素
# 的个数


# 示例
# 输入：[[1,0,1,0,0],[1,0,0,1,0],[1,1,0,0,1],[1,0,0,1,0]]
# 输出：9
# 解释：点[0,2]到点[2,4]组成一个3 * 3矩阵，对角线上全为1，其他位置全为0

# 输入：[[1,0,1,0,1],[1,0,0,1,1],[1,1,1,1,1],[1,0,0,1,0]]
# 输出：4
# 解释：点[0,2]到点[1,3]组成一个2 * 2矩阵，对角线上全为1，其他位置全为0


# 源码实现
class Solution:
    def maxSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        f = [[0] * m, [0] * m]
        up = [[0] * m, [0] * m]
        for i in range(m):
            f[0][i] = matrix[0][i]
            up[0][i] = 1 - matrix[0][i]
        edge = max(matrix[0])
        for i in range(1,n):
            f[i % 2][0] = matrix[i][0]
            up[i % 2][0] = 0 if matrix[i][0] else up[(i - 1) % 2][0] + 1
            left = 1 - matrix[i][0]
            for j in range(1, m):
                if matrix[i][j]:
                    f[i % 2][j] = min(f[(i - 1) % 2][j - 1], left, up[(i - 1) % 2][j]) + 1
                    up[i % 2][j] = 0
                    left = 0
                else:
                    f[i % 2][j] = 0
                    up[i % 2][j] = up[(i - 1) % 2][j] + 1
                    left += 1
            edge = max(edge, max(f[i % 2]))
        return edge * edge

# 主函数
if __name__ == '__main__':
    nums = [[1,0,1,0,0],[1,0,0,1,0],[1,1,0,0,1],[1,0,0,1,0]]
    s = Solution()
    print("Input: ", nums)
    print("Output: ", s.maxSquare(nums))


# 运行结果
# Input:  [[1, 0, 1, 0, 0], [1, 0, 0, 1, 0], [1, 1, 0, 0, 1], [1, 0, 0, 1, 0]]
# Output:  9