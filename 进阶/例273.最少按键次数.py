# 问题描述
# 给定一个只包含大小写字母的英文单词，问最少需要按键几次才能将单词输入(可以按caps lock以及shift键，一开始默认输入小写字母)


# 示例
# 输入：s = "Hadoop"
# 输出：最少按键次数为7

# 输入：s = "HADOOp"
# 输出：最少按键次数为8


# 源码实现
class Solution:
	def getAns(self, s):
		left = -1
		ans = 0
		ncaps = True
		for right in range(0, len(s)):
			if ncaps:
				if ord(s[right]) < 95 and right - left <= 2:
					ans += 2
					if right - left == 2:
						ncaps = False
						ans -= 1
						left = right
				else:
					left = right
					ans += 1
			else:
				if ord(s[right]) > 95 and right - left <= 2:
					ans += 2
					if right - left == 2:
						ncaps = True
						ans -= 1
						left = right
				else:
					left = right
					ans += 1
		return ans

if __name__ == '__main__':
	str = "EWlweWXZXxcscSDSDcccsdcfdsFvccDCcDCcdDcGvTvEEdddEEddEdEdAs"
	s = Solution()
	print("str:", str)
	print("最小按键次数：", s.getAns(str))


# 运行结果
# str: EWlweWXZXxcscSDSDcccsdcfdsFvccDCcDCcdDcGvTvEEdddEEddEdEdAs
# 最小按键次数： 78