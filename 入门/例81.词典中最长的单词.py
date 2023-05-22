# 问题描述
# 给出一些列字符串单词，表示一个英语词典，找到字典中最长的单词，这些单词可以通过字典中其他单词每次增加
# 一个字母构成。若有多个可能的答案，则返回字典顺序最小的那个。若没有答案，返回空字符串


# 示例
# 输入：words = ["w","wo","wor","worl","world"]
# 输出："world"
# 解释：单词"world"可以通过"w","wo","wor"和"worl"每次增加一个字母构成

# 输入：words = ["a","banana","app","appl","ap","apply","apple"]
# 输出："apple"
# 解释：单词"apply"和"apple"都能通过字典里的其他单词构成。但"apple"的字典序比"apply"小


# 数据要求
# 1 <= words <= 1000
# 1 <= words[i] <= 30


# 源码实现
class Solution:
    def longsetWord(self, words):
        words.sort()
        words.sort(key = len, reverse = True)
        res = []
        for word in words:
            temp = word
            i = 1
            for i in range(len(temp)):
                if temp[:len(temp) - i] in words:
                    if i == len(temp) - 1:
                        return temp
                    continue
                else:
                    break
        return ''

# 主函数
if __name__ == '__main__':
    solution = Solution()
    words = ["w","wo","wor","worl","world"]
    print("Input: ", words)
    print("Output: ", solution.longsetWord(words))



# 运行结果
# Input:  ['w', 'wo', 'wor', 'worl', 'world']
# Output:  world