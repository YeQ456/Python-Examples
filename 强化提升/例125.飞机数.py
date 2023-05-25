# 问题描述
# 给出飞机起飞和降落的时间列表，用序列interval表示，计算天上同时最多有多少架飞机


# 示例
# 输入：[(1,10),(2,3),(5,8),(4,7)]
# 输出：3
# 解释：第1架飞机在1时刻起飞，10时刻降落；第2架飞机在2时刻起飞，3时刻降落；第3架飞机在5时刻起飞，8时刻
# 降落；第4架飞机在4时刻起飞，7时刻降落。在5时刻到6时刻之间，天空中有3架飞机


# 源码实现
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
class Solution:
    def countOfAirplanes(self, airplanes):
        points = []
        for airplane in airplanes:
            points.append([airplane.start, 1])
            points.append([airplane.end, -1])
        number_of_airplane, max_number_of_airplane = 0, 0
        for i, count_delta in sorted(points):
            number_of_airplane += count_delta
            max_number_of_airplane = max(max_number_of_airplane, number_of_airplane)
        return max_number_of_airplane

# 主函数
if __name__ == '__main__':
    nums = [Interval(1,10),Interval(5,8),Interval(2,3),Interval(4,7)]
    s = Solution()
    print("Input: [(1,10),(2,3),(4,8),(4,7)]")
    print("Output: ", s.countOfAirplanes(nums))


# 运行结果
# Input: [(1,10),(2,3),(4,8),(4,7)]
# Output:  3