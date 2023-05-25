# 问题描述
# 给定字符串S，找到最多有k个不同字符的最长子串T，输出子串长度


# 示例
# 输入：S = "eceba", k = 3
# 输出：4
# 解释：有3个不同字符的最长子串为T = "eceb"，长度为4

# 输入：S = "WORLD", k = 4
# 输出：4
# 解释：有4个不同字符的最长子串为T = "WORL"或"ORLD"，长度为4


# 源码实现
class Solution:
    def lengthOfLongestSubstring(self, s):
        res = 0
        if s is None or len(s) == 0:
            return res
        d = {}
        tmp = 0
        start = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
            tmp = i - start + 1
            d[s[i]] = i
            res = max(res, tmp)
        return res

# 主函数
if __name__ == '__main__':
    S = 'eceba'
    s = Solution()
    print("Input: ", S)
    print("Output: ", s.lengthOfLongestSubstring(S))



# 运行结果
# Input:  eceba
# Output:  4