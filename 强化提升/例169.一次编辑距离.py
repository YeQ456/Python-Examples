# 问题描述
# 给出两个字符串S和T，判断它们是否只差1步编辑，即可变成相同的字符串


# 示例
# 输入：s = "aDb", t = "adb"
# 输出：True

# 输入：s = "ab", t = "ab"
# 输出：False


# 源码实现
class Solution:
    def isOneEditDistance(self, s, t):
        m = len(s)
        n = len(t)
        if abs(m - n) > 1:
            return False
        if m > n:
            return self.isOneEditDistance(t, s)
        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1 :] == t[i + 1 :]
                return s[i:] == t[i + 1:]
        return m != n

# 主函数
if __name__ == '__main__':
    s = "aDb"
    t = "adb"
    sol = Solution()
    print("Input: s = ", s, ", t = ", t)
    print("Output: ", sol.isOneEditDistance(s,t))


# 运行结果
# Input: s =  aDb , t =  adb
# Output:  True