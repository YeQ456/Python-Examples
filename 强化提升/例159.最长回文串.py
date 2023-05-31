# 问题描述
# 给出一个包含大小写字母的字符串，求出由这些字母构成最长的回文串长度。其中，类似"Aa"这样的不属于回文串


# 示例
# 输入：s = "abccccdd"
# 输出：7
# 解释：构造的方案是："dccaccd"


# 源码实现
class Solution:
    def longestPalindrome(self, s):
        hash = {}
        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True
        remove = len(hash)
        if remove > 0:
            remove -= 1
        return len(s) - remove

# 主函数
if __name__ == '__main__':
    nums = "abccccdd"
    s = Solution()
    print("Input: ", nums)
    print("Output: ", s.longestPalindrome(nums))


# 运行结果
# Input:  abccccdd
# Output:  7