# 问题描述
# 每个学生有两个属性编号ID和得分scores，找到每个学生最高的5个分数的平均值


# 示例
# 输入：[[1,90],[1,93],[2,93],[2,99],[2,98],[2,97],[1,62],[1,56],[2,95],[1,61]]
# 输出：1 : 72.40, 2 : 96.40
# 解释：id = 1的学生最高5个分数的平均值为(90+93+62+56+61)/5=72.40，id = 2的学生最高5个分数的平均值
# 为(93+99+98+97+95)/5=96.40

# 输入：[[1,80],[1,80],[1,80],[1,80],[1,80],[1,80]]
# 输出：1 : 80.00


# 源码实现
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
    
class Solution:
    def highFive(self, results):
        hash = dict()
        for r in results:
            if r.id not in hash:
                hash[r.id] = []
            hash[r.id].append(r.score)
            if len(hash[r.id]) > 5:
                index = 0
                for i in range(1,6):
                    if hash[r.id][id] < hash[r.id][index]:
                        index = i
                hash[r.id].pop(index)
        answer = dict()
        for id, scores in hash.items():
            answer[id] = sum(scores) / 5.0
        return answer

# 主函数
if __name__ == '__main__':
    r1 = Record(1,90)
    r2 = Record(1,93)
    r3 = Record(2,93)
    r4 = Record(2,99)
    r5 = Record(2,98)
    r6 = Record(2,97)
    r7 = Record(1,62)
    r8 = Record(1,56)
    r9 = Record(2,95)
    r10 = Record(1,61)
    list = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
    s = Solution()
    print(s.highFive(list))


# 运行结果
# {1: 72.4, 2: 96.4}