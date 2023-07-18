# 问题描述
# 给出startString和endString字符串，判断是否可以通过一系列转换将startString转变成endString。规则是只有26个小写字母，每个操作
# 只能更改一种字母。例如，若将a更改为b，则起始字符串中的所有a必须更改为b。对于每一类型的字符，可以选择转换或不转换。转换必须在
# startString中的一个字符和endString相对应的一个字符之间进行。结果返回True或False


# 示例
# 输入：startString = "abc", endString = "cde"
# 输出：True

# 输入：startString = "abc", endString = "bca"
# 输出：False


# 源码实现
class Solution:
	def canTransfer(self, startString, endString):
		if not startString and not endString:
			return True
		if len(startString) != len(endString):
			return False
		if len(set(startString)) < len(set(endString)):
			return False
		maptable = {}
		for i in range(len(startString)):
			a, b = startString[i], endString[i]
			if a in maptable:
				if maptable[a] != b:
					return False
			else:
				maptable[a] = b

		def noloopinhash(maptable):
			keyset = set(maptable)
			while keyset:
				a = keyset.pop()
				loopest = {a}
				while a in maptable:
					if a in keyset:
						keyset.remove(a)
					loopest.add(a)
					if a == maptable[a]:
						break
					a = maptable[a]
					if a in loopest:
						return False
			return True
		return noloopinhash(maptable)

if __name__ == '__main__':
	startString = "abc"
	endString = "bca"
	s = Solution()
	print("起始串：", startString)
	print("结束串：", endString)
	print("能否转换：", s.canTransfer(startString, endString))


# 运行结果
# 起始串： abc
# 结束串： bca
# 能否转换： False