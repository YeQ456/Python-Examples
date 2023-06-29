# 问题描述
# 找出给定字符串的最长子串，使得该子串中的每一个字符都出现了至少k次，返回这个子串的长度


# 示例
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为"aaa", a重复了3次


# 源码实现
class Solution:
    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

if __name__ == '__main__':
    s = Solution()
    n = "aaabb"
    k = 3
    print("输入字符串：", n)
    print("输入重复次数：", k)
    print("输出子串长度：", s.longestSubstring(n, k))


# 运行结果
# 输入字符串： aaabb
# 输入重复次数： 3
# 输出子串长度： 3