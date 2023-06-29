# 问题描述
# 有一个顺序被随机打乱的列表，代表站成一列的人群。每个人由一个二元组(h, k)表示，其中h表示身高，k表示
# 在其之前高于或等于h的人数。需要将这个队列重新排列以恢复原有的顺序


# 示例
# 输入：[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# 输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]


# 源码实现
class Solution:
    def reconstructQueue(self, people):
        queue = []
        for person in sorted(people, key = lambda _:(- _[0], _[1])):
            queue.insert(person[1], person)
        return queue

if __name__ == '__main__':
    s = Solution()
    n = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print("输入：", n)
    print("输出：", s.reconstructQueue(n))


# 运行结果
# 输入： [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
# 输出： [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]