# 问题描述
# 设计addWord(word), search(word)操作的数据结构。addWord(word)会在数据结构中添加一个单词，
# search(word)则支持普通的单词查询或只包含"."和"a~z"的简易正则表达式的查询。其中，一个"."可以
# 代表任何字母


# 示例
# 输入：addWord("a")
#       search(".")
# 输出：True

# 输入：
#      addWord("bad")
#      addWord("dad")
#      addWord("mad")
#      search("pad")
#      search("bad")
#      search(".ad")
#      search("b..")
# 输出：
#      False
#      True
#      True
#      True


# 源码实现
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_word = True
    
    def search(self, word):
        if word is None:
            return False
        return self.search_helper(self.root, word, 0)

    def search_helper(self, node, word, index):
        if node is None:
            return False
        if index >= len(word):
            return node.is_word
        
        char = word[index]
        if char != '.':
            return self.search_helper(node.children.get(char), word, index + 1)
        for child in node.children:
            if self.search_helper(node.children[child], word, index + 1):
                return True
        
        return False

# 主函数
if __name__ == '__main__':
    solution = WordDictionary()
    solution.addWord("bad")
    solution.addWord("dad")
    solution.addWord("mad")
    print('Input: addWord("bad"), addWord("dad"), addWord("mad")')
    print('Input: search("pad"), search("dad"), search(".ad"), search("b..")')
    print("Output: ", solution.search("pad"), solution.search("bad"), solution.search(".ad"), solution.search("b.."))



# 运行结果
# Input: addWord("bad"), addWord("dad"), addWord("mad")
# Input: search("pad"), search("dad"), search(".ad"), search("b..")
# Output:  False True True True