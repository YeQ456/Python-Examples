# 问题描述
# 给出一个无序的整数数组，找出其中没有出现的最小正整数


# 示例
# 输入：[1,2,0]
# 输出：3

# 输入：[3,4,-1,1]
# 输出：2


# 源码实现
class Solution:
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        if n == 0:
            return 1
        while i < n:
            while A[i] != i + 1 and A[i] <= n and A[i] > 0 and A[i] != A[A[i] - 1]:
                t = A[i]
                A[i] = A[A[i] - 1]
                A[t - 1] = t
            i = i + 1
        for i in range(n):
            if A[i] != i + 1:
                return i + 1
        return n + 1

# 主函数
if __name__ == '__main__':
    s = Solution()
    A = [3,4,-1,1]
    ans = s.firstMissingPositive(A)
    print("Input: ", A)
    print("Output: ", ans)



# 运行结果
# Input:  [1, -1, 3, 4]
# Output:  2