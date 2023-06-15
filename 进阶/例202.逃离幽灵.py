# 问题描述
# 一个简单的吃豆人游戏，起点在(0,0)，目的地是(target[0],target[1])。在地图上有几个幽灵，第i个幽灵
# 在(ghosts[i][0],ghosts[i][1])
# 在每一轮中，玩家和幽灵可以同时向东南西北4个方向之一，移动1个单位距离。当且仅当玩家在碰到任何幽灵
# 前(幽灵可能以任意的路径移动)到达终点时，能够成功逃脱。若玩家和幽灵同时到达某一个位置(包括终点)，
# 这一场游戏记为逃脱失败。若成功逃脱，返回True，否则返回False


# 示例
# 输入：ghosts = [[1,0],[0,3]], target = [0,1]
# 输出：True
# 解释：玩家可以在时间1直接到达目的地(0,1)，在位置(1,0)或(0,3)的幽灵没有办法抓到玩家


# 源码实现
class Solution:
    def escapeGohsts(self, ghosts, target):
        target_dist = abs(target[0]) + abs(target[1])
        for r,c in ghosts:
            ghosts_target = abs(target[0] - r) + abs(target[1] - c)
            if ghosts_target <= target_dist:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    num1 = [[1,0],[0,3]]
    num2 = [0,1]
    print("输入幽灵：", num1)
    print("输入目标：", num2)
    print("输出：", s.escapeGohsts(num1, num2))


# 运行结果
# 输入幽灵： [[1, 0], [0, 3]]
# 输入目标： [0, 1]
# 输出： True