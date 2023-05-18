# 问题描述
# 给定一个单词列表，返回可以在键盘的一行上使用字母键输入的单词。可以多次使用键盘中的一个字符，
# 输入字符串仅包含字母表的字母


# 示例
# 输入：["Hello", "Alaska", "Dad", "Peace"]
# 输出：["Alaska", "Dad"]
# 解释：这两个单词可以在键盘的第3行输出


# 源码实现
class Solution:
    def findWords(self, words):
        res = []
        s = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for w in words:
            for j in range(3):
                flag = 1
                for i in w:
                    if i.lower() not in s[j]:
                        flag = 0
                        break
                
                if flag == 1:
                    res.append(w)
                    break
        
        return res

# 主函数
if __name__ == '__main__':
    word = ["Hello", "Alaska", "Dad", "Peace"]
    solution = Solution()
    print("Input: word = ", word)
    print("Output: ", solution.findWords(word))



# 运行结果
# Input: word =  ['Hello', 'Alaska', 'Dad', 'Peace']
# Output:  ['Alaska', 'Dad']