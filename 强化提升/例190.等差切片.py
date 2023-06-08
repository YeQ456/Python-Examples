# 问题描述
# 若数字序列由至少3个元素组成，并任何2个连续元素之间的差值相同，则成为等差数列
# 给定由N个数字组成且下标从0开始的数组A。这个数组的一个切片指任意一个满足0 <= P < Q < N的整数
# 对(P,Q)
# 若A中的一个切片(P, Q)是等差切片，则需要满足A[P],A[P+1], ... , A[Q - 1], A[Q]是等差的。
# 也就意味着P + 1 < Q。需要实现的函数应该返回数组A中等差切片的数量


# 示例
# 输入：[1,2,3,4]
# 输出：3
# 解释：A中的3个等差切片为[1,2,3],[2,3,4]和[1,2,3,4]

# 输入：[1,2,3]
# 输出：1


# 源码实现
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        size = len(A)
        if size < 3:
            return 0
        ans = cnt = 0
        delta = A[1] - A[0]
        for x in range(2, size):
            if A[x] - A[x - 1] == delta:
                cnt += 1
                ans += cnt
            else:
                delta = A[x] - A[x - 1]
                cnt = 0
        return ans

# 主函数
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4]
    print("输入：", nums)
    print("输出：", s.numberOfArithmeticSlices(nums))


# 运行结果
# 输入： [1, 2, 3, 4]
# 输出： 3