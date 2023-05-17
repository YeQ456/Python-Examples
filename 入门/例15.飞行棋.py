# 问题描述
# 一维棋盘，起点在棋盘的最左侧，终点在棋盘的最右侧，棋盘上有几个位置和其他位置相连，若A和B相连，但
# 连接是单向，即当棋子落在位置A时，可以选择不投骰子，直接移动棋子从A到B，但不能从B移动到A。
# 给定这个棋盘的长度(length)和位置的相连情况(connections)，用一个六面的骰子(点数1~6)，问：最少
# 需要投几次才能到达终点


# 示例
# 输入：length = 10, connections = [[2,10]]
# 输出：1
# 解释：投骰子：0 -> 2,2 -> 10直接相连

# 输入：length = 15, connections = [[2,8],[6,9]]
# 输出：2
# 解释：投骰子：0 -> 6, 6 -> 9直接相连，投骰子：9 -> 15


# 源码实现
class Solution:
    # 解法一：常规解法
    def modernLudo(self, length, connections):
        ans = [i for i in range(length + 1)]
        for i in range(length + 1):
            for j in range(1,7):
                if i - j >= 0:
                    ans[i] = min(ans[i], ans[i - j] + 1)
            
            for j in connections:
                if i == j[1]:
                    ans[i] = min(ans[i], ans[j[0]])
        
        return ans[length]
    
    
    # 解法二：SPFA法
    def modernLudo(self, length, connections):
        dist = [1000000000 for i in range(100050)]
        vis = [0 for i in range(100050)]
        Q = [0 for i in range(100050)]

        st = 0
        ed = 0
        dist[1] = 0
        vis[1] = 1
        Q[ed] = 1
        ed += 1

        while(st < ed):
            u = Q[st]
            st += 1
            vis[u] = 0
            for roads in connections:
                if(roads[0] != u):
                    continue
                v = roads[1]
                if (dist[v] > dist[u]):
                    dist[v] = dist[u]
                    if(vis[u] == 0):
                        vis[v] = 1
                        Q[ed] = v
                        ed += 1
            
            for i in range(1,7):
                if(i + u > length):
                    break

                v = i + u
                if(dist[v] > dist[u] + 1):
                    dist[v] = dist[u] + 1
                    if(vis[v] == 0):
                        vis[v] = 1
                        Q[ed] = v
                        ed += 1
        
        return dist[length]
      
# 主函数
if __name__ == '__main__':
    length = 15
    connections = [[2,8],[6,9]]
    solution = Solution()
    print("Input: length = ", length, ", connections = ", connections)
    print("Output: ", solution.modernLudo(length, connections))



# 运行结果
# Input: length =  15 , connections =  [[2, 8], [6, 9]]
# Output:  2
