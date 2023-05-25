# 问题描述
# 有一个栅栏有n个柱子，现在要给柱子染色，有k种颜色，不可有超过2个相邻的柱子颜色相同，求有多少种染色
# 方案


# 示例
# 输入：n = 3, k = 2
# 输出：6
# 解释：
# 方法            柱子1            柱子2            柱子3
# 方法1            0                0               1
# 方法2            0                1               0
# 方法3            0                1               1
# 方法4            1                0               0
# 方法5            1                0               1
# 方法6            1                1               0

# 输入：n = 2, k = 2
# 输出：4
# 解释：
# 方法            柱子1            柱子2
# 方法1            0                0
# 方法2            0                1
# 方法3            1                0
# 方法4            1                1


# 源码实现
class Solution:
    def numWays(self, n, k):
        dp = [0,k,k*k]
        if n <= 2:
            return dp[n]
        if k == 1 and n >= 3:
            return 0
        for i in range(2,n):
            dp.append((k - 1) * (dp[-1] + dp[-2]))
        return dp[-1]

# 主函数
if __name__ == '__main__':
    s = Solution()
    n = 3
    k = 2
    print("Input: n = ", n, ", k = ", k)
    print("Output: ", s.numWays(n,k))


# 运行结果
# Input: n =  3 , k =  2
# Output:  6