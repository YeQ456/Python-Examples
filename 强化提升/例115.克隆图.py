# 问题描述
# 克隆一张无向图，图中的每个节点包含一个label和一个列表neighbors。保证每个节点的label均不同。返回一个
# 经过深度复制的新图，这个新图和原图具有相同的结构，并且对新图的任何改动不会对原图造成伤害


# 示例
# 序列化图{0,1,2,#,1,2,#,2,2}共有3个节点，包含2个分隔符#。第1个节点label为0，存在边从节点0链接到
# 节点1和节点2；第2个节点label为1，存在边从节点1链接到节点2；第3个节点label为2，存在边从节点2链接
# 到节点2（本身），从而形成环。如下图：
#       1
#      / \
#     /   \
#    0 --- 2
#         / \
#         \ /


# 源码实现
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
    
class Solution:
    def __init__(self):
        self.dict = {}
    
    def cloneGraph(self, node):
        if node is None:
            return None
        if node.label in self.dict:
            return self.dict[node.label]
        root = UndirectedGraphNode(node.label)
        self.dict[node.label] = root
        for item in node.neighbors:
            root.neighbors.append(self.cloneGraph(item))
        return root

# 主函数
if __name__ == '__main__':
    s = Solution()
    g0 = UndirectedGraphNode(0)
    g1 = UndirectedGraphNode(1)
    g2 = UndirectedGraphNode(2)
    g0.neighbors = [g1, g2]
    g1.neighbors = [g2]
    g2.neighbors = [g2]
    ans = s.cloneGraph(g0)
    a = [ans.label, ans.neighbors[0].label, ans.neighbors[1].label, ans.neighbors[0].neighbors[0].label, ans.neighbors[1].neighbors[0].label]
    print("Input: {0,1,2,#,1,2,#,2,2}")
    print("Output: ", a)



# 运行结果
# Input: {0,1,2,#,1,2,#,2,2}
# Output:  [0, 1, 2, 2, 2]