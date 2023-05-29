# 问题描述
# 设计一个迭代器实现摊平二维向量的功能


# 示例
# 输入：[[1,2],[3],[4,5,6]]
# 输出：[1,2,3,4,5,6]

# 输入：[[7,9],[5]]
# 输出：[7,9,5]


# 源码实现
class Vector2D(object):
    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.row, self.col = 0, -1
        self.next_elem = None
    
    def next(self):
        if self.next_elem is None:
            self.hasNext()
        temp, self.next_elem = self.next_elem, None
        return temp
    
    def hasNext(self):
        if self.next_elem:
            return True
        self.col += 1
        while self.row < len(self.vec2d) and self.col >= len(self.vec2d[self.row]):
            self.row += 1
            self.col = 0
        if self.row < len(self.vec2d) and self.col < len(self.vec2d[self.row]):
            self.next_elem = self.vec2d[self.row][self.col]
            return True
        return False

# 主函数
if __name__ == '__main__':
    nums = [[1,2],[3],[4,5,6]]
    vector2d = Vector2D(nums)
    print("Input: ", nums)
    print("Output: ")
    print(vector2d.next())
    while vector2d.hasNext():
        print(vector2d.next())


# 运行结果
# Input:  [[1, 2], [3], [4, 5, 6]]
# Output:
# 1
# 2
# 3
# 4
# 5
# 6