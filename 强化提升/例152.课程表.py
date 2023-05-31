# 问题描述
# 一共n门课程，记为0 ~ (n - 1)。有些课程在修之前需要先修另外的课程(例如，要学习课程0，需要先学课程1，
# 表示为[0,1])。现判断是否可能完成所有课程。


# 示例
# 输入：n = 2, prerequistes = [[1,0]]
# 输出：True

# 输入：n = 2, prerequistes = [[1,0],[0,1]]
# 输出：False


# 源码实现
from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        edges = {i : [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]
        for i,j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        queue, count = deque([]), 0
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            count += 1
            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.append(x)
        return count == numCourses

# 主函数
if __name__ == '__main__':
    list1 = [[1,0]]
    n = 2
    s = Solution()
    print("Input: n = ", n, ", prerequisities = ", list1)
    print("Output: ", s.canFinish(n,list1))


# 运行结果
# Input: n =  2 , prerequisities =  [[1, 0]]
# Output:  True