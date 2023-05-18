# 问题描述
# 在一个有序的数组A中寻找i，使得A[i]最接近目标数target，并输出i


# 示例
# 输入：[1,2,3], target = 2
# 输出：1
# 解释：A[1]与目标数最接近

# 输入：[1,4,6], target = 3
# 输出：1


# 源码实现
class Solution:
    def findPosition(self, A, target):
        if not A:
            return -1
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                return mid
        
        if target - A[start] < A[end] - target:
            return start
        else:
            return end

# 主函数
if __name__ == '__main__':
    generator = [1,4,6]
    target = 3
    solution = Solution()
    print("Input: nums = ", generator, ", target = ", target)
    print("Output: ", solution.findPosition(generator, target))



# 运行结果
# Input: nums =  [1, 4, 6] , target =  3
# Output:  1