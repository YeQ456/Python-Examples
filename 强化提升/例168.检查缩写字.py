# 问题描述
# 给定一个非空字符串word和缩写abbr，判断字符串是否可以和给定的缩写匹配。例如一个“word"的字符串仅包含
# 以下有效缩写：["word", "lord", "wlrd", "wold", "worl", "2rd", "w2d", "lold", "lorl", "wlrl",
# "lo2", "2rl", "3d", "w3", "4"]


# 示例
# 输入：s = "internationalization", abbr = "il2iz4n"
# 输出：True

# 输入：s = "apple", abbr = "a2e"
# 输出：False


# 源码实现
class Solution:
    def validWordAbbreviation(self, word, abbr):
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit() and abbr[j] != '0':
                start = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                i += int(abbr[start : j])
            else:
                return False
        return i == len(word) and j == len(abbr)

# 主函数
if __name__ == '__main__':
    st = "internationalization"
    abbr = "i12iz4n"
    s = Solution()
    print("Input: s = ", st, ", abbr = ", abbr)
    print("Output: ", s.validWordAbbreviation(st, abbr))


# 运行结果
# Input: s =  internationalization , abbr =  i12iz4n
# Output:  True