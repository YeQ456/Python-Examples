# 问题描述
# 使用insert和sum方法实现MapSum类。使用insert方法获取键值对（键值，整数），若键已存在，则原始键值将
# 被新键值对覆盖。使用sum方法，将获得一个表示前缀的字符串，返回以该前缀键值开头所有值的总和


# 示例
# 输入：insert("apple",3)
# 输出：null
# 输入：sum("ap")
# 输出：3

# 输入：insert("app",2)
# 输出：null
# 输入：sum("ap")
# 输出：5


# 源码实现
class TrieNode:
    def __init__(self):
        self.son = {}
        self.val = 0

class Trie:
    root = TrieNode()
    def insert(self, s, val):
        cur = self.root
        for i in range(0, len(s)):
            if s[i] not in cur.son:
                cur.son[s[i]] = TrieNode()
            cur = cur.son[s[i]]
            cur.val += val
    
    def find(self, s):
        cur = self.root
        for i in range(0, len(s)):
            if s[i] not in cur.son:
                return 0
            cur = cur.son[s[i]]
        return cur.val

class MapSum:
    def __init__(self):
        self.d = {}
        self.trie = Trie()
    
    def insert(self, key, val):
        if key in self.d:
            self.trie.insert(key, val - self.d[key])
        else:
            self.trie.insert(key, val)
        self.d[key] = val
    
    def sum(self, prefix):
        return self.trie.find(prefix)

if __name__ == '__main__':
    mapsum = MapSum()
    print("插入方法：")
    print(mapsum.insert("apple",3))
    print("求和方法：")
    print(mapsum.sum("ap"))
    print("插入方法：")
    print(mapsum.insert("app",2))
    print("求和方法：")
    print(mapsum.sum("ap"))


# 运行结果
# 插入方法：
# None
# 求和方法：
# 3
# 插入方法：
# None
# 求和方法：
# 5