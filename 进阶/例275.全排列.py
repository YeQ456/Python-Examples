# 问题描述
# 给定一个数字列表，返回其所有可能的排列


# 示例
# 输入：[1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# 源码实现
class Solution:
	def permute(self, nums):
		if nums is None:
			return []
		if nums == []:
			return [[]]
		nums = sorted(nums)
		permutation = []
		stack = [-1]
		permutations = []
		while len(stack):
			index = stack.pop()
			index += 1
			while index < len(nums):
				if nums[index] not in permutation:
					break
				index += 1
			else:
				if len(permutation):
					permutation.pop()
				continue
			stack.append(index)
			stack.append(-1)
			permutation.append(nums[index])
			if len(permutation) == len(nums):
				permutations.append(list(permutation))
		return permutations

if __name__ == '__main__':
	s = Solution()
	nums = [0,1,2]
	name = s.permute(nums)
	print("输入：", nums)
	print("输出：", name)


# 运行结果
# 输入： [0, 1, 2]
# 输出： [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]