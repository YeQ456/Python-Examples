# 问题描述
# 计算字符串中单词数，其中一个单词的定义为不含空格的连续字符串


# 示例
# 输入："Hello, my name is Jack"
# 输出：5


# 源码实现
class Solution:
    def countEnglishWords(self, str):
        ans = 0
        for i in range(len(str)):
            if str[i] != ' ' and (i == 0 or str[i - 1] == ' '):
                ans += 1
        
        return ans

# 主函数
if __name__ == '__main__':
    solution = Solution()
    s = "Hello, my name is Jack"
    print("Input: ", s)
    print("Output: ", solution.countEnglishWords(s))



# 运行结果
# Input:  Hello, my name is Jack
# Output:  5