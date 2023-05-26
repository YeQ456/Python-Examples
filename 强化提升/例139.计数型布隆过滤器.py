# 问题描述
# 实现一个计数型布隆过滤器，支持以下方法：add(string)向布隆过滤器中加入一个字符串；contains(string)
# 检查某字符是否在布隆过滤器中；remove(string)从布隆计数器中删除一个字符串


# 示例
# 输入：
# CountingBloomFilter(3)
# add("long")
# add("item")
# contains("long")
# remove("long")
# contains("long")
# 输出：
# [true,false]

# CountingBloomFilter(3)
# add("lint")
# add("lint")
# contains("lint")
# remove("lint")
# contains("lint")
# 输出：
# [true,true]


# 源码实现
import random
class HashFunction:
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed
    
    def hash(self, value):
        ret = 0
        for i in value:
            ret += self.seed * ret + ord(i)
            ret %= self.cap
        return ret

class CountingBloomFilter:
    def __init__(self, k):
        self.hashFunc = []
        for i in range(k):
            self.hashFunc.append(HashFunction(random.randint(10000,20000), i * 2 + 3))
        self.bits = [0 for i in range(20000)]
    
    def add(self, word):
        for f in self.hashFunc:
            position = f.hash(word)
            self.bits[position] += 1
        
    def remove(self, word):
        for f in self.hashFunc:
            position = f.hash(word)
            self.bits[position] -= 1
    
    def contains(self, word):
        for f in self.hashFunc:
            position = f.hash(word)
            if self.bits[position] <= 0:
                return False
        return True

# 主函数
if __name__ == '__main__':
    s = CountingBloomFilter(3)
    s.add("long")
    s.add("term")
    print("Input: ")
    print('add("long")')
    print('add("term")')
    print('contains("long")')
    print("Output: ", s.contains("long"))
    s.remove("long")
    print('remove("long")')
    print('contains("long")')
    print("Output: ", s.contains("long"))


# 运行结果
# Input: 
# add("long")
# add("term")
# contains("long")
# Output:  True
# remove("long")
# contains("long")
# Output:  False