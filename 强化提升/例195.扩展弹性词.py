# 问题描述
# 用重复扩展的字母，表达某种感情。例如, hello->heeellooo, hi->hiiii。前者对e和o进行了扩展，而后者
# 对i进行了扩展。用"组"表示一串连续相同字母。例如，abbcccaaaa的组包括a、bb、ccc、aaaa


# 示例
# 输入：S = "heeellooo", words = ["hello","hi","helo"]
# 输出：1
# 解释：可通过扩展"hello"中的"e"和"o"得到"heeellooo"，不能通过扩展"helo"得到"heeellooo"，因为
# "ll"的长度为2


# 源码实现
class Solution:
    def expressiveWords(self, S, words):
        SList = self.countGroup(S)
        n = len(SList)
        ans = 0
        for word in words:
            wordList = self.countGroup(word)
            if n != len(wordList):
                continue
            ok = 1
            for i in range(n):
                if not self.canExtend(wordList[i], SList[i]):
                    ok = 0
                    break
            ans += ok
        return ans
    
    def countGroup(self, s):
        n = len(s)
        cnt = 1
        ret = []
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                ret.append((s[i - 1], cnt))
                cnt = 1
        ret.append((s[-1], cnt))
        return ret
    
    def canExtend(self, From, To):
        return From[0] == To[0] and \
            (From[1] == To[1] or (From[1] < To[1] and To[1] >= 3))

if __name__ == '__main__':
    s = Solution()
    nums1 = "heeellooo"
    nums2 = ["hello","hi","helo"]
    print("输入：nums1 = ", nums1, ", nums2 = ", nums2)
    print("输出：", s.expressiveWords(nums1, nums2))


# 运行结果
# 输入：nums1 =  heeellooo , nums2 =  ['hello', 'hi', 'helo']
# 输出： 1