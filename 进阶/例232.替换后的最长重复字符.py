# 问题描述
# 给定一个仅包含大写英文字母的字符串，可以将字符串中的任何一个字母替换为另一个字母，最多替换k次。
# 执行上述操作后，找到最长的、只含有同一字母的子字符串长度


# 示例
# 输入："ABAB", k = 2
# 输出：4
# 解释：将两个A替换成两个B，反之亦然


# 源码实现
from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k):
        n = len(s)
        char2count = defaultdict(int)
        maxLen = 0
        start = 0
        for end in range(n):
            char2count[s[end]] += 1
            while end - start + 1 - char2count[s[start]] > k:
                char2count[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, end - start + 1)
        return maxLen

if __name__ == '__main__':
    s = Solution()
    n = "ABAB"
    m = 2
    print("输入字符串：", n)
    print("输入重复次数：", m)
    print("输出字符串长度：", s.characterReplacement(n, m))


# 运行结果
# 输入字符串： ABAB
# 输入重复次数： 2
# 输出字符串长度： 4