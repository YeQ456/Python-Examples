# 问题描述
# 给出一个可能包含重复数字的排序，求这些数字的所有排列按字典序排列后的编号从1开始


# 示例
# 输入：[1,4,2,2]
# 输出：3
# 解释：该排列是1,2,2,4数字的第3个字典序的排列

# 输入：[1,6,5,3,1]
# 输出：24
# 解释：该排列是1,1,3,5,6数字的第24个字典序的排列


# 源码实现
class Solution:
    def permutationIndex(self, A):
        if A is None or len(A) == 0:
            return 0
        index, factor, multi_fact = 1,1,1
        counter = {}
        for i in range(len(A) - 1, -1, -1):
            counter[A[i]] = counter.get(A[i], 0) + 1
            multi_fact *= counter[A[i]]
            count = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    count += 1
            index += count * factor // multi_fact
            factor *= (len(A) - i)
        return index

# 主函数
if __name__ == '__main__':
    s = Solution()
    A = [1,4,2,2]
    ans = s.permutationIndex(A)
    print("Input: ", A)
    print("Output: ", ans)



# 运行结果
# Input:  [1, 4, 2, 2]
# Output:  3