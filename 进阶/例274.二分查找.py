# 问题描述
# 给定一个升序排列的整数数组和一个要查找的整数target。用O(logn)的时间查找target第1次出现的下标(从0开始); 若target不存在于数组
# 中，返回-1


# 示例
# 输入：[1,2,3,3,4,5,10], target = 3
# 输出：2

# 输入：[1,2,3,3,4,5,10], target = 6
# 输出：-1


# 源码实现
class Solution:
	def binarySearch(self, nums, target):
		left, right = 0, len(nums) - 1
		while left + 1 < right:
			mid = (left + right) // 2
			if nums[mid] < target:
				left = mid
			else:
				right = mid
		if nums[left] == target:
			return left
		elif nums[right] == target:
			return right
		return -1

if __name__ == '__main__':
	nums = [1,3,4,5,6,9]
	target = 6
	s = Solution()
	ans = s.binarySearch(nums, target)
	print("输入数组：", nums)
	print("输入目标值：", target)
	print("输出下标位置：", ans)


# 运行结果
# 输入数组： [1, 3, 4, 5, 6, 9]
# 输入目标值： 6
# 输出下标位置： 4