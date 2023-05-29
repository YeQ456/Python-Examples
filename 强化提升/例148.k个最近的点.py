# 问题描述
# 给定一些点的坐标和一个origin的坐标，从points中找到k个离origin最近的点。按照距离由小到大返回。若两个
# 点有相同距离，则按照横坐标x值排序；若x值也相同，再按照纵坐标y值排序


# 示例
# 输入：points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0,0], k = 3
# 输出：[[1,1],[2,5],[4,4]]

# 输入：points = [[0,0],[0,9]], origin = [3,1], k = 1
# 输出：[[0,0]]


# 源码实现
import heapq
import numpy as np
np.set_printoptions(threshold = np.inf)
class Point:
    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b
    
class Solution:
    def kClosest(self, points, origin, k):
        self.heap = []
        for point in points:
            dist = self.getDistance(point, origin)
            heapq.heappush(self.heap, (-dist, -point.x, -point.y))
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        ret = []
        while len(self.heap) > 0:
            i,x,y = heapq.heappop(self.heap)
            ret.append(Point(-x, -y))
        ret.reverse()
        return ret

    def getDistance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

# 主函数
if __name__ == '__main__':
    a1 = Point(0,0)
    a2 = Point(0,9)
    nums = [a1,a2]
    origin = Point(0,0)
    k = 1
    s = Solution()
    rp = Point(0,0)
    rp = s.kClosest(nums, origin, k)
    array = [[rp[0].x, rp[0].y]]
    print("Input: [[0,0],[0,9]]", ", k = ", k)
    print("Output: ", array)


# 运行结果
# Input: [[0,0],[0,9]] , k =  1
# Output:  [[0, 0]]