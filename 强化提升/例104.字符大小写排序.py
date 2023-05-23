# 问题描述
# 给定一个只包含字母的字符串，按照先小写字母后大写字母的顺序进行排序。


# 示例
# 输入："abAcD"
# 输出："abcAD"

# 输入："ABC"
# 输出："ABC"


# 源码实现
class Solution:
    def sortLetters(self, chars):
        chars.sort(key = lambda c : c.isupper())

# 主函数
if __name__ == '__main__':
    s = Solution()
    str1 = "abAcD"
    arr = list(str1)
    s.sortLetters(arr)
    print("Input: ", str1)
    print("Output: ", ''.join(arr))



# 运行结果
# Input:  abAcD
# Output:  abcAD