# 问题描述
# 在平面中给定n个点，每一对点都是不同的，回旋镖是点的元组(i,j,k)，其中，点i和点j之间的距离与点
# i和点k之间的距离相同(i,j,k的顺序不同，为不同元组)。找到回旋镖的数量。n最多为500，并且点的坐标
# 都在[-10000, 10000]范围内


# 示例
# 输入：[[0,0],[1,0],[2,0]]
# 输出：2
# 解释：两个回旋镖是[[1,0],[0,0],[2,0]]和[[1,0],[2,0],[0,0]]


# 源码实现
class Solution:
    def getDistance(self, a, b):
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return dx * dx + dy * dy
    
    def numberOfBoomerangs(self, points):
        if points == None:
            return 0
        
        ans = 0
        for i in range(len(points)):
            disCount = {}
            for j in range(len(points)):
                if i == j:
                    continue
                distance = self.getDistance(points[i], points[j])
                count = disCount.get(distance, 0)
                disCount[distance] = count + 1
            for distance in disCount:
                ans += disCount[distance] * (disCount[distance] - 1)
        
        return ans

# 主函数
if __name__ == '__main__':
    solution = Solution()
    n = [[0,0],[1,0],[2,0]]
    print("Input: n = ", n)
    print("Output: ", solution.numberOfBoomerangs(n))



# 运行结果
# Input: n =  [[0, 0], [1, 0], [2, 0]]
# Output:  2