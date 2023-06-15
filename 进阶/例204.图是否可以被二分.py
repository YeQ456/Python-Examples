# 问题描述
# 给定一个无向图graph，当这个图被二分时（二部图），输出True。若一个图是二部图，则表示可以将图里的点
# 集分为两个独立的子集A和B，并且图中所有的边都是一个端点属于A，另一个端点属于B。
# 给定一个图，graph[i]为一个列表，表示与节点i有边相连的节点。这个图一共有graph.length个节点，
# 从0到graph.length - 1.图中没有自边或重复的边，即graph[i]中不包含i也不包含某个点两次以上


# 示例
# 输入：[[1,3],[0,2],[1,3],[0,2]]
# 输出：True
# 解释：
# 0 ---- 1
# |      |
# |      |
# 3 ---- 2
# 可以把图分为{0, 2}和{1,3}两部分，并且各自内部没有连线


# 源码实现
class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        self.color = [0] * n
        for i in range(n):
            if self.color[i] == 0 and not self.colored(i, graph, 1):
                return False
        return True
    
    def colored(self, now, graph, c):
        self.color[now] = c
        for nxt in graph[now]:
            if self.color[nxt] == 0 and not self.colored(nxt, graph, -c):
                return False
            elif self.color[nxt] == self.color[now]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    num = [[1,3],[0,2],[1,3],[0,2]]
    print("输入：", num)
    print("输出：", s.isBipartite(num))


# 运行结果
# 输入： [[1, 3], [0, 2], [1, 3], [0, 2]]
# 输出： True