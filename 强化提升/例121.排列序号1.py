# 问题描述
# 给出一个不含重复数字的排列，求这些数字所有排列按字典序排序后的编号。编号从1开始


# 示例
# 输入：[1,2,4]
# 输出：1
# 解释：该排列是1,2,4三个数字的第1个字典序的排列

# 输入：[3,2,1]
# 输出：6
# 解释：该排列是1，2,3三个数字的第6个字典序的排列


# 源码实现
class Solution:
    def permutationIndex(self, A):
        result = 1
        factor = 1
        for i in range(len(A) - 1, -1, -1):
            rank = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    rank += 1
            result += factor * rank
            factor *= len(A) - i
        return result

# 主函数
if __name__ == '__main__':
    s = Solution()
    A = [3,2,1]
    ans = s.permutationIndex(A)
    print("Input: ", A)
    print("Output: ", ans)



# 运行结果
# Input:  [3, 2, 1]
# Output:  6