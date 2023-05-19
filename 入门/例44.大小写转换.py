# 问题描述
# 将一个字符由小写字母转换为大写字母


# 示例
# 输入：a
# 输出：A

# 输入：b
# 输出：B


# 源码实现
class Solution:
    def lowercaseToUppercase(self, character):
        # ASCII码中小写字母对应的大写字母相差32
        return chr(ord(character) - 32)

# 主函数
if __name__ == '__main__':
    solution = Solution()
    ans = solution.lowercaseToUppercase('a')
    print("Input: a")
    print("Output: ", ans)



# 运行结果
# Input: a
# Output:  A