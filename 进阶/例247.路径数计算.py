# 问题描述
# 输入一个矩阵的长度为1，宽度为w，并指定3个必经点，问有多少种方法可以从左上角走到右下角（每一步只能
# 向右或向下走）。答案对1000000007取模


# 示例
# 给出l = 4, w = 4, 3个必经点：[1,1]、[2,2]、[3,3]
# 返回：8

# 给出l = 1, w = 5, 3个必经点：[1,2]、[1,3]、[1,4]
# 返回：1


# 源码实现
class Point:
    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b
    
class Solution:
    def calculationTheSumOfPath(self, l, w, points):
        points.sort(key = lambda point: point.x)
        if points[0].x != 1 or points[0].y != 1:
            points = [Point(1,1)] + points
        if points[0].x != l or points[0].y != w:
            points = points + [Point(l,w)]
        arr = [[] for i in range(len(points) - 1)]
        maxl = 0
        maxw = 0
        for i in range(1, len(points)):
            l = points[i].x - points[i - 1].x
            w = points[i].y - points[i - 1].y
            arr[i - 1] = [points[i].x - points[i - 1].x, points[i].y - points[i - 1].y]
            maxl = max(maxl, l)
            maxw = max(maxw, w)
        dp = [[0 for i in range(max(maxl, maxw) + 1)] for j in range(max(maxl, maxw) + 1)]
        del l, w, maxl, maxw
        for i in range(len(dp)):
            for j in range(i, len(dp)):
                if i == 0:
                    dp[j][i] = dp[i][j] = 1
                else:
                    dp[j][i] = dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        ans = 1
        for i in arr:
            ans = ans * dp[i[0]][i[1]] % 1000000007
        return ans

if __name__ == '__main__':
    l = 43
    w = 48
    points = [Point(17,19), Point(43, 48), Point(3, 5)]
    s = Solution()
    print("长与宽分别为：", l, w)
    print("路径种数：", s.calculationTheSumOfPath(l, w, points))


# 运行结果
# 长与宽分别为： 43 48
# 路径种数： 472542024