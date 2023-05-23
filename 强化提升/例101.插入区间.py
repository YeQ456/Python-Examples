# 问题描述
# 给出一个无重叠、按照区间起始端点排序的列表。在列表中插入一个新的区间，确保列表中的区间仍然有序且
# 不重叠(若有必要，可合并区间)


# 示例
# 输入：(2,5), 插入[(1,2),(5,9)]
# 输出：[(1,9)]

# 输入：(3,4)，插入[(1,2),(5,9)]
# 输出：[(1,2),(3,4),(5,9)]


# 源码实现
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def get(self):
        str1 = "(" + str(self.start) + "," + str(self.end) + ")"
        return str1
    
    def equals(self, Intervalx):
        if self.start == Intervalx.start and self.end == Intervalx.end:
            return 1
        else:
            return 0

class Solution:
    def insert(self, intervals, newInterval):
        results = []
        insertPos = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                results.append(interval)
                insertPos += 1
            elif interval.start > newInterval.end:
                results.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        results.insert(insertPos, newInterval)
        return results

# 主函数
if __name__ == '__main__':
    s = Solution()
    Interval1 = Interval(1,2)
    Interval2 = Interval(5,9)
    Interval3 = Interval(2,5)
    result = s.insert([Interval1,Interval2],Interval3)
    print("Input: [", Interval1.get(), ",", Interval2.get(), "]", " ", Interval3.get())
    print("Output: [", result[0].get(), "]")



# 运行结果
# Input: [ (1,2) , (5,9) ]   (1,9)
# Output: [ (1,9) ]