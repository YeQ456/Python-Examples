# 问题描述
# 写一个方法，输入给定字符串，返回将这个字符串的字母逐个翻转后的新字符串


# 示例
# 输入：hello
# 输出：olleh


# 源码实现
class Solution:
    def reverseString(self, s):
        return s[::-1]

# 主函数
if __name__ == '__main__':
    x = "hello"
    print("Input: ", x)
    print("Output: ", Solution().reverseString(x))



# 运行结果
# Input:  hello
# Output:  olleh