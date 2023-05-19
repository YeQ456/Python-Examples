# 问题描述
# 写出一个函数，判断两个字符串是否可以通过改变字母的顺序，变成一样的字符串


# 示例
# 输入：s = "ab", t = "ab"
# 输出：True

# 输入：s = "abcd", t = "dcba"
# 输出：True

# 输入：s = "ac", t = "ab"
# 输出：False


# 源码实现
class Solution:
    def anagram(self, s, t):
        set_s = [0] * 256
        set_t = [0] * 256
        for i in range(0, len(s)):
            set_s[ord(s[i])] += 1
        for i in range(0, len(t)):
            set_t[ord(t[i])] += 1
        for i in range(0, 256):
            if set_s[i] != set_t[i]:
                return False
        
        return True

# 主函数
if __name__ == '__main__':
    solution = Solution()
    s = "abcd"
    t = "dcba"
    ans = solution.anagram(s, t)
    print("Input: s = ", s, ", t = ", t)
    print("Output: ", ans)



# 运行结果
# Input: s =  abcd , t =  dcba
# Output:  True