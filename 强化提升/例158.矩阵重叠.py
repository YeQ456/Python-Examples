# 问题描述
# 给定两个矩阵，判断这两个矩阵是否有重叠。其中l1代表第一个矩阵的左上角，r1代表第一个矩阵的右下角；l2
# 代表第二个矩阵的左上角，r2代表第二个矩阵的右下角。只要满足l1 != r2并且l2 != r1，两个矩阵就没有
# 重叠的部分，否则就有重叠的部分


# 示例
# 输入：l1 = [0,8], r1 = [8,0], l2 = [6,6], r2 = [10,0]
# 输出：True

# 输入：[0,8], r1 = [8,0], l2 = [9,6], r2 = [10,0]
# 输出：False


# 源码实现
class Point:
    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b

class Solution:
    def doOverlap(self, l1, r1, l2, r2):
        if l1.x > r2.x or l2.x > r1.x:
            return False
        if l1.y < r2.y or l2.y < r1.y:
            return False
        return True

# 主函数
if __name__ == '__main__':
    l1 = Point(0,8)
    r1 = Point(8,0)
    l2 = Point(6,6)
    r2 = Point(10,0)
    s = Solution()
    print("Input1: l1 = (0,8), r1 = (8,0)")
    print("Input2: l2 = (6,6), r2 = (10,0)")
    print("Output: ", s.doOverlap(l1,r1,l2,r2))


# 运行结果
# Input1: l1 = (0,8), r1 = (8,0)
# Input2: l2 = (6,6), r2 = (10,0)
# Output:  True