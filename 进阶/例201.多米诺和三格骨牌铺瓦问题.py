# 问题描述
# 有两种瓷砖：一种2X1多米诺形状，用2个并排的相同字母表示; 一种"L"形三格骨牌形状，用3个排成L形的相同
# 字母表示。形状可以旋转。给定N，有多少种方法可以铺完一块2XN的地板？返回答案对(10^9 + 7)取模之后
# 的结果。每个方格都必须被铺盖


# 示例
# 输入：3
# 输出：5
# 解释：以下5种方法，不同的字母表示不同的瓷砖：
# 1.XYZ
#   XYZ
# 2.XXZ
#   YYZ
# 3.XYY
#   XZZ
# 4.XXY
#   XYY
# 5.XYY
#   XXY


# 源码实现
class Solution:
    def numTilings(self, N):
        if N < 3:
            return N
        MOD = 1000000007
        f = [[0,0,0] for i in range(N + 1)]
        f[0][0] = f[1][0] = f[1][1] = f[1][2] = 1
        for i in range(2, N + 1):
            f[i][0] = (f[i - 1][0] + f[i - 2][0] + f[i - 2][1] + f[i - 2][2]) % MOD
            f[i][1] = (f[i - 1][0] + f[i - 1][2]) % MOD
            f[i][2] = (f[i - 1][0] + f[i - 1][1]) % MOD
        return f[N][0]

if __name__ == '__main__':
    s = Solution()
    nums = 3
    print("输入：", nums)
    print("输出：", s.numTilings(nums))


# 运行结果
# 输入： 3
# 输出： 5