# 问题描述
# 给出两个一维向量，实现一个迭代器，交替返回两个向量的元素


# 示例
# 输入：v1 = [1,2], v2 = [3,4,5,6]
# 输出：[1,3,2,4,5,6]

# 输入：v1 = [1,1,1,1], v2 = [3,4,5,6]
# 输出：[1,3,1,4,1,5,1,6]


# 源码实现
class ZigzagIterator:
    def __init__(self, v1, v2):
        self.queue = [v for v in (v1, v2) if v]
    
    def next(self):
        v = self.queue.pop(0)
        value = v.pop(0)
        if v:
            self.queue.append(v)
        return value
    
    def hasNext(self):
        return len(self.queue) > 0

# 主函数
if __name__ == "__main__":
    v1 = [1,2]
    v2 = [3,4,5,6]
    print("Input: ")
    print(",".join(str(i) for i in v1))
    print(",".join(str(i) for i in v2))
    s, result = ZigzagIterator(v1, v2), []
    while s.hasNext():
        result.append(s.next())
    print("Output: ", result)


# 运行结果
# Input: 
# 1,2
# 3,4,5,6
# Output:  [1, 3, 2, 4, 5, 6]