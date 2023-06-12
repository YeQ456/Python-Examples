# 问题描述
# 在一个有向图中，从某个节点开始，每次沿着图的有向边走。若到达一个终端节点则停止。
# 对于自然数K，若任何行走的路线，都可以在少于K步的情况下停在终端节点，则“最终是安全的”。判断哪些节点
# 最终是安全的，返回它们升序排列的数组
# 有向图具有N个节点，其标签为0,1,...,N-1，其中N是图的长度。该图以下面的形式给出：graph[i]是从i出发，
# 通过边(i,j)，所有能够到达的节点j组成的链表


# 示例
# 输入：[[1, 2], [2, 3], [5], [0], [5], [], []]
# 输出：[2,4,5,6]
# 解释：节点5和6就是出度为0，因为graph[5]和graph[6]均为空。除了没有出度的节点5和6，节点2和4都只能
# 到达节点5，而节点5本身就是安全状态点，所以2和4也为安全状态点了。


# 源码实现
class Solution:
    def eventualSafeNodes(self, graph):
        def dfs(graph, i, visited):
            for j in graph[i]:
                if j in visited:
                    return False
                if j in ans:
                    continue
                visited.add(j)
                if not dfs(graph, j, visited):
                    return False
                visited.remove(j)
            ans.add(i)
            return True
        ans = set()
        for i in range(len(graph)):
            visited = set([i])
            dfs(graph, i, visited)
        return sorted(list(ans))

if __name__ == '__main__':
    s = Solution()
    nums = [[1,2],[2,3],[5],[0],[5],[],[]]
    print("输入：", nums)
    print("输出：", s.eventualSafeNodes(nums))


# 运行结果
# 输入： [[1, 2], [2, 3], [5], [0], [5], [], []]
# 输出： [2, 4, 5, 6]