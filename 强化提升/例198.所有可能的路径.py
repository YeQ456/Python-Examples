# 问题描述
# 给定N个节点的有向无环图。查找从节点0到节点N - 1的所有可能的路径，以任意顺序返回。该图给出方式：节点
# 为0,1，。。。，graph.length - 1. graph[i]是一个列表，其中任意一个元素j表示图中含有一条i -> j的
# 有向边


# 示例
# 输入：[[1,2],[3],[3],[]]
# 输出：[[0,1,3],[0,2,3]]
# 解释：一共有0 -> 1 -> 3和0 -> 2 -> 3两条路径
# 0 -> 1
# |    |
# 2 -> 3


# 源码实现
class Solution:
    def allPathsSourceTarget(self, graph):
        N = len(graph)
        res = []
        def dfs(N, graph, start, res, path):
            if start == N - 1:
                res.append(path)
            else:
                for node in graph[start]:
                    dfs(N, graph, node, res, path + [node])
        dfs(N, graph, 0, res, [0])
        return (res)

if __name__ == '__main__':
    s = Solution()
    nums = [[1,2],[3],[3],[]]
    print("输入：", nums)
    print("输出：", s.allPathsSourceTarget(nums))


# 运行结果
# 输入： [[1, 2], [3], [3], []]
# 输出： [[0, 1, 3], [0, 2, 3]]