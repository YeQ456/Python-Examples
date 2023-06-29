# 问题描述
# 给定给定一个整数数组A，长度为n。Bk为A中元素顺时针旋转k个位置后得到的新数组。定义关于A的轮转函数F如下
# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n - 1) * Bk[n - 1]。计算F(0),F(1), ... , F(n - 1)中
# 的最大值


# 示例
# 输入：[4,3,2,6]
# 输出：26
# 解释：
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
# 所以F(0), F(1), F(2), F(3)中最大值为F(3)，即26


# 源码实现
class Solution:
    def maxRotateFunction(self, A):
        s = sum(A)
        curr = sum(i * a for i, a in enumerate(A))
        maxVal = curr
        for i in range(1, len(A)):
            curr += s - len(A) * A[-i]
            maxVal = max(maxVal, curr)
        return maxVal

if __name__ == '__main__':
    s = Solution()
    n = [4,3,2,6]
    print("输入：", n)
    print("输出：", s.maxRotateFunction(n))


# 运行结果
# 输入： [4, 3, 2, 6]
# 输出： 26