# 问题描述
# 给出一个由小写字母组成的字符串S，将这个字符串分割成尽可能多的部分，使得每个字母最多出现在一部分中，
# 并返回每部分的长度


# 示例
# 输入：s = "ababcbacadefegdhijhklij"
# 输出：[9,7,8]
# 解释：划分后为："ababcbaca"，"defegde", "hijhklij"


# 源码实现
class Solution(object):
    def partitionLabels(self, S):
        last = {c:i for i, c in enumerate(S)}
        right = left = 0
        ans = []
        for i, c in enumerate(S):
            right = max(right, last[c])
            if i == right:
                ans.append(i - left + 1)
                left = i + 1
        return ans

if __name__ == '__main__':
    s = Solution()
    ss = "ababcbacadefegdhijhklij"
    print("输入：", ss)
    print("输出：", s.partitionLabels(ss))


# 运行结果
# 输入： ababcbacadefegdhijhklij
# 输出： [9, 6, 8]