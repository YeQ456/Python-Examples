# 问题描述
# 若一个单词通过循环右移可获得另外一个单词，则称该单词为循环单词。给出一个单词集合，统计该集合中有多少
# 种循环单词。所有单词均为小写


# 示例
# 输入：dict = ["picture", "turepic", "icturep", "word", "ordw", "long"]
# 输出：3
# 解释："picture"、"turepic"、"icturep"是相同的循环单词，"word"、"ordw"也相同


# 源码实现
class Solution:
    def countRotateWords(self, words):
        dict1 = set()
        for w in words:
            s = w + w
            for i in range(0, len(w)):
                tmp = s[i:i+len(w)]
                if tmp in dict1:
                    dict1.remove(tmp)
            dict1.add(w)
        return len(dict1)

# 主函数
if __name__ == '__main__':
    dict1 = ["picture", "turepic", "icturep", "word", "ordw", "long"]
    s = Solution()
    print("输入：", dict1)
    print("输出：", s.countRotateWords(dict1))


# 运行结果
# 输入： ['picture', 'turepic', 'icturep', 'word', 'ordw', 'long']
# 输出： 3