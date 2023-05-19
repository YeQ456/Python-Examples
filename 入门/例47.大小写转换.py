# 问题描述
# 将一个字符串中的小写字母转换为大写字母，非字母的字符不发生变化


# 示例
# 输入：str = "abc"
# 输出："ABC"

# 输入：str = "aBc"
# 输出："ABC"

# 输入：str = "abC12"
# 输出："ABC12"


# 源码实现
class Solution:
    def lowercaseToUppercase(self, str):
        p = list(str)
        for i in range(len(p)):
            if p[i] >= 'a' and p[i] <= 'z':
                p[i] = chr(ord(p[i]) - 32)
        
        return ''.join(p)

# 主函数
if __name__ == '__main__':
    solution = Solution()
    s1 = "abC12"
    ans = solution.lowercaseToUppercase(s1)
    print("Input: str = ", s1)
    print("Output: ", ans)



# 运行结果
# Input: str =  abC12
# Output:  ABC12