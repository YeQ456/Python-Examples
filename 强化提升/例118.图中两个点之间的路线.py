# 问题描述
# 给出一张有向图，设计一个算法判断两个点s和t之间是否存在路线


# 示例
# 如下所示
# 输入：s = B, t = E
# 输出：True

# 输入：s = D, t = C
# 输出：False

#       A -----> B -----> C
#        \       |
#         \      |
#          \     |
#           \    |
#            \   |
#             \  |
#              \ |
#               \|
#                D -----> E


# 源码实现
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def dfs(self, i, countrd, graph, t):
        if countrd[i] == 1:
            return False
        if i == t:
            return True
        countrd[i] = 1
        for j in i.neighbors:
            if countrd[j] == 0 and self.dfs(j, countrd, graph, t):
                return True
        return False

    def hasRoute(self, graph, s, t):
        countrd = {}
        for x in graph:
            countrd[x] = 0
        return self.dfs(s, countrd, graph, t)

# 主函数
if __name__ == '__main__':
    s = Solution()
    gA = DirectedGraphNode('A')
    gB = DirectedGraphNode('B')
    gC = DirectedGraphNode('C')
    gD = DirectedGraphNode('D')
    gE = DirectedGraphNode('E')
    gA.neighbors = [gB, gD]
    gB.neighbors = [gC, gD]
    gD.neighbors = [gE]
    graph = [gA,gB,gC,gD,gE]
    ans = s.hasRoute(graph, gB, gE)
    print("Input: {A,B,C,D,E,A#B,A#D,B#C,B#D,D#E}, B, E")
    print("Output: ", ans)



# 运行结果
# Input: {A,B,C,D,E,A#B,A#D,B#C,B#D,D#E}, B, E
# Output:  True