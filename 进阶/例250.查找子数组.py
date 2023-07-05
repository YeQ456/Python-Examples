# 问题描述
# 给定一个数组arr和一个正整数k，需要从这个数组中找到一个连续子数组，使得这个子数组的和为k。返回这个子
# 数组的长度。若有多个这样的子数组，返回结束位置最小的；若结束位置最小的也有多个，返回结束位置最小且
# 起始位置最小的。若找不到这样的子数组，返回-1


# 示例
# 输入：arr = [1,2,3,4,5], k = 5
# 输出：2

# 输入：arr = [3,5,7,10,2], k = 12
# 输出：2


# 源码实现
class Solution:
    def searchSubarray(self, arr, k):
        sum = 0
        maps = {}
        maps[sum] = 0
        st = len(arr) + 5
        lent = 0
        for i in range(0, len(arr)):
            sum += arr[i]
            if sum - k in maps:
                if st > maps[sum - k]:
                    st = maps[sum - k]
                    lent = i + 1 - maps[sum - k]
            if sum not in maps:
                maps[sum] = i + 1
        if st == len(arr) + 5:
            return -1
        else:
            return lent

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    k = 5
    s = Solution()
    print("数组：", arr, " k为：", k)
    print("最短和为k的子数组：", s.searchSubarray(arr, k))


# 运行结果
# 数组： [1, 2, 3, 4, 5]  k为： 5
# 最短和为k的子数组： 2