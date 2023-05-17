# 问题描述
# 给定两个字符串s和t，每次可以任意交换s的奇数位或偶数位上的字符，即奇数位上的字符能够与其他奇数位的
# 字符交换，偶数位上的字符也能与其他偶数位的字符互换，问：能否经过若干次交换，使s变成t


# 示例
# 输入：s = "abcd", t = "cdab"
# 输出：Yes
# 解释：第一次a与c交换，第二次b与d交换

# 输入：s = "abcd", t = "bcda"
# 输出：No
# 解释：无论怎么交换，都无法得到bcda


# 源码实现
class Solution:
    def isTwin(self, s, t):
        if len(s) != len(t):
            return "No"
        
        oddS = []                 # s数组的奇数位
        evenS = []                # s数组的偶数位
        oddT = []                 # t数组的奇数位
        evenT = []                # t数组的偶数位

        for i in range(len(s)):
            if i & 1:
                oddS.append(s[i])
                oddT.append(t[i])
            else:
                evenS.append(s[i])
                evenT.append(t[i])
        
        oddS.sort()               # 对数组进行排序
        oddT.sort()               
        evenS.sort()
        evenT.sort()

        for i in range(len(oddS)):
            if oddS[i] != oddT[i]:
                return "No"
        
        for i in range(len(evenS)):
            if evenS[i] != evenT[i]:
                return "No"
        
        return "Yes"

# 主函数
if __name__ == '__main__':
    s = "abcd"
    t = "cbad"
    solution = Solution()
    print("Input: s = ", s, ", t = ", t)
    print("Output: ", solution.isTwin(s,t))



# 运行结果
# Input: s =  abcd , t =  cbad
# Output:  Yes