# 问题描述
# 在x轴和y轴确定的二维空间中，x轴的上方有许多气球。提供每个气球在x轴上投影的起点和终点坐标。起点总是
# 小于终点，最多有10^4个气球
# 可以沿着x轴从不同点垂直向上发射箭头。若xstart <= x <= xend，则坐标为xstart和xend的气球被从x处发射
# 的箭头戳爆。可以发射的箭头数量没有限制，一次射击的箭头一直无限地向上移动。找到戳破所有气球的最小
# 发射箭头数


# 示例
# 输入气球在x轴的投影起点和终点坐标为[[10,16],[2,8],[1,6],[7,12]]
# 输出：2
# 解释：一种方法在[2,6]之间发射一个箭头，爆破气球[2,8]和[1,6]，在[10,12]之间发射另一个箭头，爆破另外
# 2个气球


# 源码实现
class Solution(object):
    def findMinArrowShots(self, points):
        if points == None or not points:
            return 0
        points.sort(key = lambda x:x[1])
        ans = 1
        lastEnd = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > lastEnd:
                ans += 1
                lastEnd = points[i][1]
        return ans

if __name__ == '__main__':
    s = Solution()
    n = [[10,16],[2,8],[1,6],[7,12]]
    print("输入：", n)
    print("输出：", s.findMinArrowShots(n))


# 运行结果
# 输入： [[10, 16], [2, 8], [1, 6], [7, 12]]
# 输出： 2