# 问题描述
# 需要上n门课才能获得学位，这些课标号为0~(n-1)。有些课需要先完成先修课。现在给定课程的数量和先修课要求，
# 返回为了完成所有课程所安排的学习顺序(可任意).若不能完成所有课程，返回空数组


# 示例
# 输入：n = 2, prerequisites = [[1,0]]
# 输出：[0,1]

# 输入：n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# 输出：[0,1,2,3]或[0,2,1,3]


# 源码实现
from queue import Queue
class Solution:
    def findOrder(self, numCourses, prerequisites):
        edges = {i : [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        queue = Queue(maxsize = numCourses)
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.put(i)
        order = []
        while not queue.empty():
            node = queue.get()
            order.append(node)
            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.put(x)
        if len(order) == numCourses:
            return order
        return []

# 主函数
if __name__ == '__main__':
    n = 4
    list1 = [[1,0],[2,0],[3,1],[3,2]]
    s = Solution()
    print("Input: n = ",n,", prerequisities = ", list1)
    print("Output: ", s.findOrder(n,list1))


# 运行结果
# Input: n =  4 , prerequisities =  [[1, 0], [2, 0], [3, 1], [3, 2]]
# Output:  [0, 1, 2, 3]