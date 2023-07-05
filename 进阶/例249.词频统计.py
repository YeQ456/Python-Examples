# 问题描述
# 输入一个字符串s和一个字符串列表excludeList，求s中不存在于excludeList中的所有最高词频


# 示例
# 输入：s = "I love Amazon.", excludeList = []
# 输出：["i", "love", "amazon"]

# 输入：s = "Do not trouble trouble", excludeList = ["do"]
# 输出：["trouble"]


# 源码实现
class Solution:
    def getWords(self, s, excludeList):
        s = s.lower()
        words = []
        p = ''
        for letter in s:
            if letter < 'a' or letter > 'z':
                if p != '':
                    words.append(p)
                p = ''
            else:
                p += letter
        if p != '':
            words.append(p)
        dic = {}
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        ans = []
        mx = 0
        for word in words:
            if dic[word] > mx and (not word in excludeList):
                mx = dic[word]
                ans = [word]
            elif dic[word] == mx and word not in ans and not word in excludeList:
                ans.append(word)
        return ans

if __name__ == '__main__':
    s = "Do do do do not not Trouble trouble."
    excludeList = ["do"]
    s = Solution()
    print("待查句子：", s, "除外词表为：", excludeList)
    print("词频最高的单词：", s.getWords(s, excludeList))


# 运行结果
# 待查句子：Do do do do not not Trouble trouble. 除外词表为：['do']
# 词频最高的单词：['not', 'trouble']