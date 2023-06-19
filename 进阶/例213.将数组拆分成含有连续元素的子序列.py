# 问题描述
# 给定一个整数数组nums,将nums拆分成若干（至少2个）子序列，并每个子序列至少包含3个连续的整数，返回是否
# 能实现这样的拆分


# 示例
# 输入：[1,2,3,3,4,5]
# 输出：True
# 解释：可拆分为子序列：[1,2,3],[3,4,5]

# 输入：[1,2,3,3,4,4,5,5]
# 输出：True

# 输入：[1,2,3,4,4,5]
# 输出：False


# 源码实现
class Solution:
    def isPossible(self, nums):
        cnt, tail = {}, {}
        for num in nums:
            cnt[num] = cnt[num] + 1 if num in cnt else 1
        for num in nums:
            if not num in cnt or cnt[num] < 1:
                continue
            if num - 1 in tail and tail[num - 1] > 0:
                tail[num - 1] -= 1
                tail[num] = tail[num] + 1 if num in tail else 1
            elif num + 1 in cnt and cnt[num + 1] > 0 and num + 2 in cnt and cnt[num + 2] > 0:
                cnt[num + 1] -= 1
                cnt[num + 2] -= 1
                tail[num + 2] = tail[num + 2] + 1 if num + 2 in tail else 1
            else:
                return False
            cnt[num] -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,3,4,5]
    print("输入：", nums)
    print("输出：", s.isPossible(nums))


# 运行结果
# 输入： [1, 2, 3, 3, 4, 5]
# 输出： True