# 问题描述
# 两个具有相同非零长度的整数序列A和B，可以交换它们的一些元素A[i]和B[i]，两个可交换的元素在它们各自的
# 序列中处于相同的索引位置。进行交换后，A和B需要严格递增。给定A和B，返回使两个序列严格递增的最小交换
# 次数。


# 示例
# 输入：A = [1,3,5,4], B = [1,2,3,7]
# 输出：1
# 解释：可以交换A[3]和B[3]，两个序列变为A = [1,3,5,7]和B = [1,2,3,4]


# 源码实现
class Solution:
    def minSwap(self, A, B):
        if len(A) == 0 or len(A) != len(B):
            return 0
        non_swapped, swapped = [0] * len(A), [1] + [0] * (len(A) - 1)
        for i in range(1, len(A)):
            swps, no_swps = set(), set()
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                swps.add(swapped[i - 1] + 1)
                no_swps.add(non_swapped[i - 1])
            if B[i - 1] < A[i] and A[i - 1] < B[i]:
                swps.add(non_swapped[i - 1] + 1)
                no_swps.add(swapped[i - 1])
            swapped[i], non_swapped[i] = min(swps), min(no_swps)
        return min(swapped[-1], non_swapped[-1])

if __name__ == '__main__':
    s = Solution()
    nums1 = [1,3,5,4]
    nums2 = [1,2,3,7]
    print("输入：nums1 = ", nums1, ", nums2 = ", nums2)
    print("输出：", s.minSwap(nums1, nums2))


# 运行结果
# 输入：nums1 =  [1, 3, 5, 4] , nums2 =  [1, 2, 3, 7]
# 输出： 1