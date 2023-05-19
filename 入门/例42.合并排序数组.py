# 问题描述
# 合并两个有序的整数数组A和B，形成一个新的有序数组


# 示例
# 输入：[1,2,3], [4,5]
# 输出：[1,2,3,4,5]

# 输入：[1,2,5], [3,4]
# 输出：[1,2,3,4,5]


# 源码实现
class Solution:
    def mergeSortedArray(self, A, m, B, n):
        i, j = m - 1, n - 1
        t = len(A) - 1
        while i >= 0 or j >= 0:
            if i < 0 or (j >= 0 and B[j] > A[i]):
                A[t] = B[j]
                j -= 1
            else:
                A[t] = A[i]
                i -= 1
            t -= 1

# 主函数
if __name__ == '__main__':
    solution = Solution()
    A = [1,2,3,0,0]
    m = 3
    B = [4,5]
    n = 2
    solution.mergeSortedArray(A,m,B,n)
    print("Input: A = ", A, ", m = ", m, ", B = ", B, ", n = ", n)
    print("Output: ", A)



# 运行结果
# Input: A =  [1, 2, 3, 4, 5] , m =  3 , B =  [4, 5] , n =  2
# Output:  [1, 2, 3, 4, 5]