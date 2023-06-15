# 问题描述
# 有n个城市由航班连接，每个航班(u,v,w)表示从城市u出发，到达城市v，价格为w。给定城市数目n和所有的航班
# flights。找到从起点src到终点站dst线路最便宜的价格。旅途中最多只能中转K次。若没有找到合适的路线，
# 返回-1


# 示例
# 输入：n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0
# 输出：500
# 解释：不中转则最便宜的价格为500


# 源码实现
import sys
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        distance = [sys.maxsize for i in range(n)]
        distance[src] = 0
        for i in range(0, K + 1):
            dN = list(distance)
            for u, v, c in flights:
                dN[v] = min(dN[v], distance[u] + c)
            distance = dN
        if distance[dst] != sys.maxsize:
            return distance[dst]
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    K = 0
    print("输入城市：", n)
    print("输入航班：", flights)
    print("输入出发地：", src)
    print("输入目的地：", dst)
    print("输入中转数：", K)
    print("输出价格：", s.findCheapestPrice(n, flights, src, dst, K))


# 运行结果
# 输入城市： 3
# 输入航班： [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
# 输入出发地： 0
# 输入目的地： 2
# 输入中转数： 0
# 输出价格： 500