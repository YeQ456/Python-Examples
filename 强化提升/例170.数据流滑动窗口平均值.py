# 问题描述
# 给出一串整数流和窗口大小，计算滑动窗口中所有整数的平均值


# 示例
# 定义MovingAverage m = new MovingAverage(3)，则m.next(1) = 1
# 返回：1.00000；m.next(10) = (1 + 10) / 2，返回5.50000; m.next(3) = (1 + 10 + 3) / 3
# 返回4.66667; m.next(5) = (10 + 3 + 5) / 3，返回6.00000


# 源码实现
from collections import deque
class MovingAverage(object):
    def __init__(self, size):
        self.queue = deque([])
        self.size = size
        self.sum = 0.0

    def next(self, val):
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
        self.sum += val
        self.queue.append(val)
        return self.sum / len(self.queue)

# 主函数
if __name__ == '__main__':
    s = MovingAverage(3)
    print("Input: 1,10,3,5")
    print("Input1: ", s.next(1))
    print("Input2: ", s.next(10))
    print("Input3: ", s.next(3))
    print("Input4: ", s.next(5))


# 运行结果
# Input: 1,10,3,5
# Input1:  1.0
# Input2:  5.5
# Input3:  4.666666666666667
# Input4:  6.0