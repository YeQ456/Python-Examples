# 问题描述
# 现在有1个01字符串str，寻找最长的01连续子串(即0和1交替出现，如0101010101)。可以对字符串进行一些操作，使得01连续子串尽可能长。
# 操作是指选择一个位置，将字符串断开，变成两个字符串，然后每个字符串翻转，最后按照原来的顺序拼接在一起。可以进行0次或多次上述
# 操作，返回最终能够获得的最大01连续子串的长度。


# 示例
# 输入：str = "100010010"
# 输出：5

# 输入：str = "1001"
# 输出：2


# 源码实现
class Solution:
	def TheLongest01Substring(self, str):
		str += str
		ans = 1
		cnt = 1
		for i in range(1, len(str)):
			if str[i] != str[i - 1]:
				cnt += 1
			else:
				cnt = 1
			if ans < cnt and 2 * cnt <= len(str):
				ans = cnt
		return ans

if __name__ == '__main__':
	str = "1001"
	s = Solution()
	print("二进制串：", str)
	print("最长01子串有：", s.TheLongest01Substring(str), "个")


# 运行结果
# 二进制串： 1001
# 最长01子串有： 2个