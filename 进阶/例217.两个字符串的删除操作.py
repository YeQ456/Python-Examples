# 问题描述
# 给定word1和word2两个单词，找到使word1和word2相同所需的最少步骤，每个步骤可以删除任一字符串中的一个
# 字符。


# 示例
# 输入："sea"和"eat"
# 输出：2
# 解释：第1步将"sea"变成"ea"，第2步"eat"变成"ea"


# 源码实现
class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (word1[i] == word2[j]))
        return m + n - 2 * dp[m][n]

if __name__ == '__main__':
    s = Solution()
    word1 = "sea"
    word2 = "eat"
    print("输入1：", word1)
    print("输入2：", word2)
    print("输出：", s.minDistance(word1, word2))


# 运行结果
# 输入1： sea
# 输入2： eat
# 输出： 2