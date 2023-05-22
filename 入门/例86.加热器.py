# 问题描述
# 设计一个具有固定加热半径的加热器。已知所有房屋和热水器所处的位置，它们分布在一条水平线上。找出最小
# 的加热半径，使得所有房屋都处在至少一个加热器的加热范围内。输入所有房屋和加热器所处位置，输出加热器
# 最小的加热半径。


# 示例
# 输入：房屋位置[1,2,3], 加热器位置[2]
# 输出：1
# 解释：唯一的一个加热器放在2的位置，只要加热器半径为1，加热范围就能覆盖到所有房屋了


# 源码实现
class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        ans = 0
        for house in houses:
            ans = max(ans, self.closestHeater(house, heaters))
        return ans
    
    def closestHeater(self, house, heaters):
        start = 0
        end = len(heaters) - 1
        while start + 1 < end:
            m = start + (end - start) // 2
            if heaters[m] == house:
                return 0
            elif heaters[m] < house:
                start = m
            else:
                end = m
        
        return min(abs(house - heaters[start]), abs(heaters[end] - house))

# 主函数
if __name__ == '__main__':
    s = Solution()
    num = [1,2,3]
    h = [2]
    print("Input: num = ", num, ", h = ", h)
    print("Output: ", s.findRadius(num, h))



# 运行结果
# Input: num =  [1, 2, 3] , h =  [2]
# Output:  1