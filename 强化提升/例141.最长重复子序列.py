# 问题描述
# 给出一个字符串，找到最长重复子序列。若这样的序列有2个，这2个子序列不能在同一个位置有同一个元素。（在
# 2个子序列中的第i个元素，不能在原来的字符串中有相同的下标）


# 示例
# 输入："aab"
# 输出：1
# 解释：2个子序列是a(第1个)和a(第2个)。

# 输入："abc"
# 输出：0


# 源码实现
class Solution:
    def longestRepeatingSubsequence(self, str):
        n = len(str)
        dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if str[i - 1] == str[j - 1] and i != j:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[n][n]

# 主函数
if __name__ == '__main__':
    s = Solution()
    str1 = "abcaa"
    print("Input: ", str1)
    print("Output: ", s.longestRepeatingSubsequence(str1))


# 运行结果
# Input:  abcaa
# Output:  2   