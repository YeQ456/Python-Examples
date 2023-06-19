# 问题描述
# 给定字符串和字符串字典，找到字典中可以通过删除给定字符串的某些字符所形成的最长字符串。若有多个可能
# 的结果，则返回具有最小字典顺序的最长单词。若没有可能的结果，则返回空字


# 示例
# 输入：s = "abpcplea", d = ["ale", "apple", "monkey", "plea"]
# 输出：apple


# 源码实现
class Solution:
    def findLongestWord(self, s, d):
        for x in sorted(d, key = lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in x):
                return x
        return ''

if __name__ == '__main__':
    s = "abpcplea"
    d = ["ale", "apple", "monkey", "plea"]
    ss = Solution()
    print("输入：", s)
    print("输入：", d)
    print("输出：", ss.findLongestWord(s,d))


# 运行结果
# 输入： abpcplea
# 输入： ['ale', 'apple', 'monkey', 'plea']
# 输出： apple