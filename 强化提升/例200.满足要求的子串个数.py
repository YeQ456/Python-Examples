# 问题描述
# 给定一个字符串S和一个单词字典words，判断words中一共有多少个单词words[i]是字符串S的子序列。子序列
# 不同于子串，子序列不要求连续


# 示例
# 输入：S = "abcde", words = ["a", "bb", "acd", "ace"]
# 输出：3
# 解释：words内有3个单词是S的子串：a、acd、ace


# 源码实现
class Solution:
    def numMatchingSubseq(self, S, words):
        self.idx = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7,
                    'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15,
                    'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23,
                    'y':24, 'z':25}
        n = len(S)
        nxtPos = []
        tmp = [-1] * 26
        for i in range(n - 1, -1, -1):
            tmp[self.idx[S[i]]] = i
            nxtPos.append([i for i in tmp])
        nxtPos = nxtPos[::-1]
        ans = 0
        for word in words:
            if self.isSubseq(word, nxtPos):
                ans += 1
        return ans
    
    def isSubseq(self, word, nxtPos):
        lenw = len(word)
        lens = len(nxtPos)
        i, j = 0, 0
        while i < lenw and j < lens:
            j = nxtPos[j][self.idx[word[i]]]
            if j < 0:
                return False
            i += 1
            j += 1
        return i == lenw
    
if __name__ == '__main__':
    s = Solution()
    str1 = "abcde"
    str2 = ["a", "bb", "acd", "ace"]
    print("输入字符串：", str1)
    print("输入子串：", str2)
    print("输出：", s.numMatchingSubseq(str1, str2))


# 运行结果
# 输入字符串： abcde
# 输入子串： ['a', 'bb', 'acd', 'ace']
# 输出： 3