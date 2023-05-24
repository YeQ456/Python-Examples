# 问题描述
# 给定一个有向图，图节点的拓扑排序定义如下：(1)对图中的每一条有向边A->B，在拓扑排序中A一定在B之前；(2)
# 拓扑排序中第1个节点可以是图中的任何一个没有其他节点指向它的节点。针对给定的有向图找到任意一种拓扑排序
# 的顺序


# 示例
#               1 ----> 4
#              /       /
#             /       /
#            0 ----> 2
#             \     / \
#              \   /   \  
#                3 ---> 5
#
# 上图的拓扑排序可以为：
# [0,1,2,3,4,5]
# [0,2,3,1,5,4]


# 源码实现
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
    
class Solution:
    def topSort(self, graph):
        indegree = {}
        for x in graph:
            indegree[x] = 0
        for i in graph:
            for j in i.neighbors:
                indegree[j] += 1
        ans = []
        for i in graph:
            if indegree[i] == 0:
                self.dfs(i, indegree, ans)
        return ans
    
    def dfs(self, i, indegree, ans):
        ans.append(i.label)
        indegree[i] -= 1
        for j in i.neighbors:
            indegree[j] -= 1
            if indegree[j] == 0:
                self.dfs(j, indegree, ans)

# 主函数
if __name__ == '__main__':
    s = Solution()
    g0 = DirectedGraphNode(0)
    g1 = DirectedGraphNode(1)
    g2 = DirectedGraphNode(2)
    g3 = DirectedGraphNode(3)
    g4 = DirectedGraphNode(4)
    g5 = DirectedGraphNode(5)
    g0.neighbors = [g1, g2, g3]
    g1.neighbors = [g4]
    g2.neighbors = [g4, g5]
    g3.neighbors = [g4, g5]
    graph = [g0, g1, g2, g3, g4, g5]
    result = s.topSort(graph)
    print("Input: 如例图")
    print("Output: ", result)



# 运行结果
# Input: 如例图
# Output:  [0, 1, 2, 3, 4, 5]