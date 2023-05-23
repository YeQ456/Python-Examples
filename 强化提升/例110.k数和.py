# 问题描述
# 给定n个不同的正整数，整数k(1 <= k <= n)及一个目标数字。在这n个数里找出k个数，使得这k个数的和等于
# 目标数字。


# 示例
# 输入：[1,2,3,4], k = 2, target = 5
# 输出：[[1,4],[2,3]]

# 输入：[1,3,4,6], k = 3, target = 8
# 输出：[[1,3,4]]


# 源码实现
class Solution:
    def kSumII(self, A, k, target):
        anslist = []
        self.dfs(A, k, target, 0, [], anslist)
        return anslist

    def dfs(self, A, k, target, index, onelist, anslist):
        if target == 0 and k == 0:
            anslist.append(onelist)
            return
        if len(A) == index or target < 0 or k < 0:
            return
        self.dfs(A, k, target, index + 1, onelist, anslist)
        self.dfs(A, k - 1, target - A[index], index + 1, onelist + [A[index]], anslist)

# 主函数
if __name__ == '__main__':
    s = Solution()
    A = [1,2,3,4]
    k = 2
    target = 5
    result = s.kSumII(A, k, target)
    print("Input: A = ", A, ", k = ", k, ", target = ", target)
    print("Output: ", result)



# 运行结果
# Input: A =  [1, 2, 3, 4] , k =  2 , target =  5
# Output:  [[2, 3], [1, 4]]