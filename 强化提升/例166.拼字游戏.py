# 问题描述
# 给定一个2D矩阵，包含a ~ z和字典dict,找到矩阵上最大的单词集合（这些单词不能在相同的位置重叠），返回
# 最大集合的大小。字典中的单词不重复；可以重复使用字典中的单词


# 示例
# 输入如下矩阵：
# [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
# dict = ["abc", "cfi", "beh", "defi", "gh"]
# 输出：3
# 解释：得到最大的集合为["abc","defi", "gh"]


# 源码实现
import collections
class TrieNode(object):
    def __init__(self, value = 0):
        self.value = value
        self.isWord = False
        self.children = collections.OrderedDict()
    
    @classmethod
    def insert(cls, root, word):
        p = root
        for c in word:
            child = p.children.get(c)
            if not child:
                child = TrieNode(c)
                p.children[c] = child
            p = child
        p.isWord = True

class Solution:
    def boggleGame(self, board, words):
        self.board = board
        self.words = words
        self.m = len(board)
        self.n = len(board[0])
        self.results = []
        self.temp = []
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.root = TrieNode()
        for word in words:
            TrieNode.insert(self.root, word)
        self.dfs(0, 0, self.root)
        return len(self.results)
    
    def dfs(self, x, y, root):
        for i in range(x, self.m):
            for j in range(y, self.n):
                paths = []
                temp = []
                self.getAllPaths(i, j, paths, temp, root)
                for path in paths:
                    word = ''
                    for px, py in path:
                        word += self.board[px][py]
                        self.visited[px][py] = True
                    self.temp.append(word)
                    if len(self.temp) > len(self.results):
                        self.results = self.temp[:]
                    self.dfs(i, j, root)
                    self.temp.pop()
                    for px, py in path:
                        self.visited[px][py] = False
            y = 0

    def getAllPaths(self, i, j, paths, temp, root):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or \
            self.board[i][j] not in root.children or \
            self.visited[i][j] == True:
            return
        root = root.children[self.board[i][j]]
        if root.isWord:
            temp.append((i,j))
            paths.append(temp[:])
            temp.pop()
            return
        self.visited[i][j] = True
        deltas = [(0,1),(0,-1),(1,0),(-1,0)]
        for dx, dy in deltas:
            newx = i + dx
            newy = j + dy
            temp.append((i,j))
            self.getAllPaths(newx, newy, paths, temp, root)
            temp.pop()
        self.visited[i][j] = False

# 主函数
if __name__ == '__main__':
    nums = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    dictw = ["abc", "cfi", "beh", "defi", "gh"]
    s = Solution()
    print("Input: ", nums, ", dictw = ", dictw)
    print("Output: ", s.boggleGame(nums, dictw))


# 运行结果
# Input:  [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']] , dictw =  ['abc', 'cfi', 'beh', 'defi', 'gh']
# Output:  3