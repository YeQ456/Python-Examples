# 问题描述
# 有N个网络节点，从1到N标记。给定times，一个传输时间和有向边列表times[i] = (u, v, w)，其中u是起点，
# v是目标点，w是一个信号从起点到目标点花费的时间。从一个特定节点K发出信号，计算所有节点收到信号需要
# 花费多长时间; 若不可能，返回-1


# 示例
# 输入：times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# 输出：2
# 解释：节点2到节点1的时间为1，节点2到节点3的时间为1，节点2到节点4的时间为2，所以最长花费时间为2


# 源码实现
class Solution:
    def networkDelayTime(seld, times, N, K):
        INF = 0x3f3f3f3f
        G = [[INF for i in range(N + 1)] for j in range(N + 1)]
        for i in range(1, N + 1):
            G[i][i] = 0
        for i in range(0, len(times)):
            G[times[i][0]][times[i][1]] = times[i][2]
        dis = G[K][:]
        vis = [0] * (N + 1)
        for i in range(0, N - 1):
            Mini = INF
            p = K
            for j in range(1, N + 1):
                if vis[j] == 0 and dis[j] < Mini:
                    Mini = dis[j]
                    p = j
            vis[p] = 1
            for j in range(1, N + 1):
                if vis[j] == 0 and dis[j] > dis[p] + G[p][j]:
                    dis[j] = dis[p] + G[p][j]
        ans = 0
        for i in range(1, N + 1):
            ans = max(ans, dis[i])
        if ans == INF:
            return -1
        return ans

if __name__ == '__main__':
    s = Solution()
    times = [[2,1,1],[2,3,1],[3,4,1]]
    N = 4
    K = 2
    print("输入时间矩阵：", times)
    print("输入网络大小：", N)
    print("输入起始点：", K)
    print("最小花费：", s.networkDelayTime(times, N, K))


# 运行结果
# 输入时间矩阵： [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
# 输入网络大小： 4
# 输入起始点： 2
# 最小花费： 2