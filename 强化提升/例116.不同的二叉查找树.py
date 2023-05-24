# 问题描述
# 给定正整数n，求以1~n为节点组成的不同的二叉查找树有几种？


# 示例
# 输入：n = 3,
# 输出：5
# 解释：
# 1            3          3             2            1
#  \          /          /             / \            \
#   3        2          1             1   3            2
#  /        /            \                              \
# 2        1              2                              3


# 源码实现
class Solution:
    def numTree(self, n):
        dp = [1,1,2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n - 2)]
            for i in range(3, n + 1):
                for j in range(1, i + 1):
                    dp[i] += dp[j - 1] * dp[i - j]
            return dp[n]

# 主函数
if __name__ == '__main__':
    s = Solution()
    n = 3
    ans = s.numTree(n)
    print("Input: n = ", n)
    print("Output: ", ans)



# 运行结果
# Input: n =  3
# Output:  5