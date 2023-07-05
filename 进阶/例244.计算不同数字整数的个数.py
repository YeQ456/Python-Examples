# 问题描述
# 给定非负整数n，计算小于等于n位数。具有不同数字字符的所有整数共有多少个


# 示例
# 输入：2
# 输出：91
# 解释：0 <= x < 100范围内的总数，除去[11,22,33,44,55,66,77,88,99]共91个


# 源码实现
class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        n = min(n, 10)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 9
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (11 - i)
        return sum(dp)

if __name__ == '__main__':
    s = Solution()
    x = 2
    print("输入: ", x)
    print("输出：", s.countNumbersWithUniqueDigits(2))


# 运行结果
# 输入:  2
# 输出： 91