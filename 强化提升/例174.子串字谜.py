# 问题描述
# 给定一个字符串s和一个非空字符串p，找到在s中所有关于p的字谜起始索引。字符串仅由小写英文字母组成，
# 字符串s和p的长度不大于40000


# 示例
# 输入：s = "cbaebabacd", p = "abc"
# 输出：[0,6]
# 解释：子串起始索引index = 0是"cba"，为"abc"的字谜。子串起始索引index = 6是"bac"是"abc"的字谜


# 源码实现
class Solution:
    def findAnagrams(self, s, p):
        ans = []
        sum = [0 for x in range(0,30)]
        plength = len(p)
        slength = len(s)
        for i in range(plength):
            sum[ord(p[i]) - ord('a')] += 1
        start = 0
        end = 0
        matched = 0
        while end < slength:
            if sum[ord(s[end]) - ord('a')] >= 1:
                matched += 1
            sum[ord(s[end]) - ord('a')] -= 1
            end += 1
            if matched == plength:
                ans.append(start)
            if end - start == plength:
                if sum[ord(s[start]) - ord('a')] >= 0:
                    matched -= 1
                sum[ord(s[start]) - ord('a')] += 1
                start += 1
        return ans

# 主函数
if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    ss = Solution()
    print("Input: s = ", s, ", p = ", p)
    print("Output: ", ss.findAnagrams(s,p))


# 运行结果
# Input: s =  cbaebabacd , p =  abc
# Output:  [0, 6]