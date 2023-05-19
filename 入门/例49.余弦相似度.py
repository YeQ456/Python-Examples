# 问题描述
# 余弦相似性是指内积空间两个矢量之间的相似性度量，计算它们之间角度的余弦。0°的余弦为1，对于任何其他角度，
# 余弦小于1.用公式可以表示为
#
#                                      A · B           ∑ Ai × Bi
#            similarity = cos(θ) = ———————————— = ————————————————————
#                                   ||A|| ||B||    √(∑(Ai)² × ∑(Bi)²)
#
# 给定两个向量A和B，求出它们的余弦相似度。若余弦相似不合法(例如 A = [0], B = [0])，返回2


# 示例
# 输入：A = [1], B = [2]
# 输出：1.000


# 源码实现
import math
class Solution:
    def cosineSimilarity(self, A, B):
        if len(A) != len(B):
            return 2
        n = len(A)
        up = 0
        for i in range(n):
            up += A[i] * B[i]
        down = sum(a * a for a in A) * sum(b * b for b in B)
        if down == 0:
            return 2
        return up / math.sqrt(down)

# 主函数
if __name__ == '__main__':
    A = [1,4,0]
    B = [1,2,3]
    solution = Solution()
    print("Input: A = ", A, ", B = ", B)
    print("Output: ", solution.cosineSimilarity(A,B))



# 运行结果
# Input: A =  [1, 4, 0] , B =  [1, 2, 3]
# Output:  0.583383351196948