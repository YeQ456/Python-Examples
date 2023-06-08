# 问题描述
# 给定字符串s，找出s中最长回文序列的长度，假设s的最大长度为1000


# 示例
# 输入："bbbab"
# 输出：4
# 解释：其中一个可能的最长回文序为"bbbb"

# 输入："bbbbb"
# 输出：5


# 源码实现
class Solution:
    def longestPalindromeSubseq(self, s):
        length = len(s)
        if length == 0:
            return 0
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][length - 1]

# 主函数
if __name__ == '__main__':
    str1 = "bbbab"
    s = Solution()
    print("输入：", str1)
    print("输出：", s.longestPalindromeSubseq(str1))


# 运行结果
# 输入： bbbab
# 输出： 4