# 问题描述
# 有一个01字符串str,只会出现3个单词，两个字节的单词10或11，一个字节的单词0，判断字符串中最后一个
# 单词的字节数


# 示例
# 输入：str = "100"
# 输出：1
# 解释：str由两个单词构成，10和0

# 输入：str = "1110"
# 输出：2
# 解释：str由两个单词构成，11和10


# 源码实现
class Solution:
    def judgeTheLastNumber(self, str):
        if str[-1] == 1:
            return 2
        for i in range(-2, -len(str) -1, -1):
            if str[i] == 0:
                return -1 * ((i * (-1) + 1) % 2) + 2
        
        return -1 * (len(str) % 2) + 2

# 主函数
if __name__ == '__main__':
    str = "111110"
    solution = Solution()
    print("Input: str = ", str)
    print("Output: ", solution.judgeTheLastNumber(str))



# 运行结果
# Input: str =  111110
# Output:  2