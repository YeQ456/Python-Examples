# 问题描述
# 根据以下规则缩写单词：只保留首尾字母，中间缩写以中间部分的字符串长度表示。
# 例如：
# (1) it ---- it(没有缩写)
# (2) d|uc|k ---- d2k(缩去2个字符)
# (3) s|omentim|e ---- s6e(缩去6个字符)
# 假设有一个字典和一个单词，判断这个单词的缩写在字典中是否唯一


# 示例
# 输入：["deer", "door", "cake", "card"]，字典中所有单词的缩写为["d2r","d2r","c2e","c2d"]
# isUnique("dear")输出为False; isUnique("cart")输出为True; isUnique("cane")输出为False;
# isUnique("make")输出为True


# 源码实现
class ValidWordAbbr:
    def __init__(self, dictionary):
        self.map = {}
        for word in dictionary:
            abbr = self.word_to_abbr(word)
            if abbr not in self.map:
                self.map[abbr] = set()
            self.map[abbr].add(word)
    
    def word_to_abbr(self, word):
        if len(word) <= 1:
            return word
        return word[0] + str(len(word[1:-1])) + word[-1]

    def isUnique(self, word):
        abbr = self.word_to_abbr(word)
        if abbr not in self.map:
            return True
        for word_in_dict in self.map[abbr]:
            if word != word_in_dict:
                return False
        return True

# 主函数
if __name__ == '__main__':
    dic = ["deer", "door", "cake", "card"]
    s = ValidWordAbbr(dic)
    print("输入字典：", dic)
    print("输入单词：dear")
    print("输出：", s.isUnique("dear"))
    print("输入单词：cart")
    print("输出：", s.isUnique("cart"))


# 运行结果
# 输入字典： ['deer', 'door', 'cake', 'card']
# 输入单词：dear
# 输出： False
# 输入单词：cart
# 输出： True