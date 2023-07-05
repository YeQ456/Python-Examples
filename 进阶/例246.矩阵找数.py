# 问题描述
# 给出一个矩阵mat，找出所有行都出现的数字。若有多个，输出最小的那个数；若没有，则输出-1


# 示例
# 输入：mat = [[1,2,3],[3,4,1],[2,1,3]]
# 输出：1

# 输入：mat = [[1,2,3],[3,4,2],[2,1,8]]
# 输出：2


# 源码实现
class Solution:
    def findingNumber(self, mat):
        hashSet = {}
        n = len(mat)
        for mati in mat:
            vis = {}
            for x in mati:
                vis[x] = 1
            for key in vis:
                if key not in hashSet:
                    hashSet[key] = 0
                hashSet[key] += 1
        ans = 100001
        for i in hashSet:
            if hashSet[i] == n:
                ans = min(i, ans)
        return -1 if ans == 100001 else ans

if __name__ == '__main__':
    mat = [[1,2,3],[3,4,1],[2,1,3]]
    s = Solution()
    print("矩阵：", mat)
    print("每一行都出现的最小的数：", s.findingNumber(mat))


# 运行结果
# 矩阵： [[1, 2, 3], [3, 4, 1], [2, 1, 3]]
# 每一行都出现的最小的数： 1