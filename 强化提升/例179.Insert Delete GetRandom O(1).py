# 问题描述
# 设计一个数据结构实现以下所有操作。insert(val)，若元素不在集合中，则插入。remove(val)，若元素在
# 集合中，则从集合中移除。getRandom()，随机从集合中返回一个元素，每个元素返回的概率相同


# 示例
# RandomizedSetrandomSet = new RandomizedSet(), 初始化一个空集合
# randomSet.insert(1), 1成功插入集合中，返回True
# randomSet.remove(2), 返回False, 2不在集合中
# randomSet.insert(2), 2插入集合中，返回True，set现在有[1,2]
# randomSet.getRandom(), 随机返回1或2
# randomSet.remove(1), 从集合中移除1，返回True
# randomSet.insert(2), 2已经在集合中，返回True
# randomSet.getRandom(), 2是集合中唯一的数字，则getRandom总是返回2


# 源码实现
import random
class RandomizedSet(object):
    def __init__(self):
        self.nums, self.pos = [], {}
    
    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
    
    def remove(self, val):
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop()
            del self.pos[val]
            return True
        return False
    
    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]

# 主函数
if __name__ == '__main__':
    s = RandomizedSet()
    print("插入一个元素：1")
    print(s.insert(1))
    print("移除一个元素：2")
    print(s.remove(2))
    print("插入一个元素：2")
    print(s.insert(2))
    print("获取随机元素：1")
    print(s.getRandom())
    print("移除一个元素：1")
    print(s.remove(1))
    print("插入一个元素：2")
    print(s.insert(2))


# 运行结果
# 插入一个元素：1
# True
# 移除一个元素：2
# False
# 插入一个元素：2
# True
# 获取随机元素：1
# 2
# 移除一个元素：1
# True
# 插入一个元素：2
# False