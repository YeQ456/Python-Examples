# 问题描述
# 给定一个数组，在数组中寻找2个数，使它们的和最接近但不超过目标值，并返回它们的和


# 示例
# 输入：target = 15, array = [1,3,5,11,7]
# 输出：14
# 解释：11 + 3 = 14 < 15

# 输入：target = 16, array = [1,3,5,11,7]
# 输出：16
# 解释：11 + 5 = 16 <= 16


# 源码实现
class Solution:
    def closestTargetNumber(self, target, array):
        size = len(array)
        if size < 2:
            return -1
        
        array.sort()
        diff = 0x7fffffff
        left = 0
        right = size - 1

        while left < right:
            if array[left] + array[right] > target:
                right -= 1
            else:
                diff = min(diff, target - array[left] - array[right])
                left += 1
        
        if diff == 0x7fffffff:
            return -1
        else:
            return target - diff

# 主函数
if __name__ == '__main__':
    array = [1,3,5,11,7]
    target = 15
    solution = Solution()
    print("Input: array = ", array, ", target = ", target)
    print("Output: ", solution.closestTargetNumber(target,array))



# 运行结果
# Input: array =  [1, 3, 5, 11, 7] , target =  15
# Output:  14