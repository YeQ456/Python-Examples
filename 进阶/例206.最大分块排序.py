# 问题描述
# 数组arr是[0,1,...,arr.length - 1]的一个排列。将数组拆分成若干"块"(分区),并单独对每个块进行排序，使得
# 连接这些块后，结果为排好的升序数组，问最多可以分多少块？


# 示例
# 输入：arr = [1,0,2,3,4]
# 输出：4
# 解释：可以将数组分解为：[1,0],[2],[3],[4]


# 源码实现
class Solution(object):
    def maxChunksToSorted(self, arr):
        def dfs(cur, localmax):
            visited[cur] = True
            localmax = max(localmax, cur)
            if not visited[arr[cur]]:
                return dfs(arr[cur], localmax)
            return localmax
        visited = [False] * len(arr)
        count = 0
        i = 0
        while i < len(arr):
            localmax = dfs(i, -1)
            i += 1
            while i < localmax + 1:
                if not visited[i]:
                    localmax = dfs(i, localmax)
                i += 1
            count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    arr = [1,0,2,3,4]
    print("输入：", arr)
    print("输出：", s.maxChunksToSorted(arr))


# 运行结果
# 输入： [1, 0, 2, 3, 4]
# 输出： 4