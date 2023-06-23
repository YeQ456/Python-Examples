# 问题描述
# 给定M X N个元素的矩阵(M行，N列)，以对角线顺序返回矩阵的所有元素。给定矩阵的元素总数不会超过10000


# 示例
# 输入：
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# 输出：[1,2,4,7,5,3,6,8,9]


# 源码实现
class Solution:
    def findDiagonalOrder(self, matrix):
        import collections
        result = []
        dd = collections.defaultdict(list)
        if not matrix:
            return result
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dd[i + j + 1].append(matrix[i][j])
        for k, v in dd.items():
            if k % 2 == 1:
                dd[k].reverse()
            result += dd[k]
        return result

if __name__ == '__main__':
    m = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    s = Solution()
    print("输入：", m)
    print("输出：", s.findDiagonalOrder(m))


# 运行结果
# 输入： [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出： [1, 2, 4, 7, 5, 3, 6, 8, 9]