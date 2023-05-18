# 问题描述
# 输入两个字符串s和t，判断s能否在删除一些字符后得到t


# 示例
# 输入：s = "abc", t = "c"
# 输出：True
# 解释：删除a和b即可得到t

# 输入：s = "a", t = "c"
# 输出：False


# 源码实现
class Solution:
    def canGetString(self, s, t):
        pos = 0
        for x in t:
            while pos < len(s) and s[pos] != x:
                pos += 1
            if pos == len(s):
                return False
            pos += 1
        
        return True

# 主函数
if __name__ == '__main__':
    s = "abc"
    t = "c"
    solution = Solution()
    print("Input: s = ", s, ", t = ", t)
    print("Output: ", solution.canGetString(s,t))



# 运行结果
# Input: s =  abc , t =  c
# Output:  True