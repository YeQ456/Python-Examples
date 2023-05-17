# 问题描述
# 给定一个整数数组A。定义B[i] = A[0] * ... * A[i - 1] * A[i + 1] * ... * A[n - 1], 即B[i]为剔除
# A[i]元素后所有数组元素之积，计算数组B时尽可能不使用除法，最后输出B


# 示例
# 输入：A = [1,2,3]
# 输出：B = [6,3,2]
# 解释：B[0] = A[1] * A[2] = 6; B[1] = A[0] * A[2] = 3; B[2] = A[0] * A[1] = 2

# 输入：A = [2,4,6]
# 输出：B = [24,12,8]


# 源码实现
class Solution:
    def productExclude(self, A):
        length, B = len(A), []
        f = [0 for i in range(length + 1)]
        f[length] = 1

        for i in range(length - 1, 0, -1):
            f[i] = f[i + 1] * A[i]
        
        tmp = 1
        for i in range(length):
            B.append(tmp * f[i + 1])
            tmp *= A[i]
        
        return B

# 主函数
if __name__ == '__main__':
    solution = Solution()
    A = [1,2,3,4]
    B = solution.productExclude(A)
    print("Input: A = ", A)
    print("Output: B = ", B)



# 运行结果
# Input: A =  [1, 2, 3, 4]
# Output: B =  [24, 12, 8, 6]