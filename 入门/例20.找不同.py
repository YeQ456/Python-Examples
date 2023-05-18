# 问题描述
# 给定两个只包含小写字母的字符串s和t。字符串t由随机打乱字符顺序的字符串s在随机位置添加一个字符生成，
# 找出在t中添加的字符


# 示例
# 输入：s = "abcd", t = "abcde"
# 输出：e


# 源码实现
class Solution:
    def findTheDifference(self, s, t):
        flag = 0
        for i in range(len(s)):
            # 计算不同字符的ASCII码之差
            flag += (ord(t[i])) - (ord(s[i]))
        
        flag += ord(t[-1])
        return chr(flag)

# 主函数
if __name__ == '__main__':
    solution = Solution()
    s = "abcd"
    t = "abcde"
    print("Input: s = ", s, ", t = ", t)
    print("Output: ", solution.findTheDifference(s,t))



# 运行结果
# Input: s =  abcd , t =  abcde
# Output:  e