# 问题描述
# 给定一个非负数数组，表示一个整数，在该整数的基础上加1，返回一个新数组。数字按照数位高低进行排列，最高位的数在列表最前面


# 示例
# 输入：[1,2,3]
# 输出：[1,2,4]

# 输入：[9,9,9]
# 输出：[1,0,0,0]


# 源码实现
class Solution:
	def plusOne(self, digits):
		digits = list(reversed(digits))
		digits[0] += 1
		i, carry = 0,0
		while i < len(digits):
			next_carry = (digits[i] + carry) // 10
			digits[i] = (digits[i] + carry) % 10
			i, carry = i + 1, next_carry
		if carry > 0:
			digits.append(carry)
		return list(reversed(digits))

if __name__ == '__main__':
	s = Solution()
	num = [9,9,9]
	ans = s.plusOne(num)
	print("输入：", num)
	print("输出：", ans)


# 运行结果
# 输入： [9, 9, 9]
# 输出： [1, 0, 0, 0]