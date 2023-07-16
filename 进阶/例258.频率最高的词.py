# 问题描述
# 给出一个字符串s，表示小说的内容，再给出一个不参加统计的单词列表list，求字符串中出现频率最高的单词（若有多个，返回字典序最小的单词）


# 示例
# 输入：s = "Jimmy has an apple, it is on the table, he like it", excludeWords = ["a", "an", "the"]
# 输出：it


# 源码实现
class Solution:
	def frequentWord(self, s, excludewords):
		map = {}
		while len(s) > 0:
			end = s.find(' ') if s.find(' ') > -1 else len(s)
			word = s[:end] if s[end - 1].isalpha() else s[:end - 1]
			s = s[end + 1:]
			if word not in excludewords:
				if word in map:
					map[word] += 1
				else:
					map[word] = 1
		max = -1
		res = []
		for key, val in map.items():
			if val == max:
				res.append(key)
			elif val > max:
				max = val
				res = [key]
		res.sort()
		return res[0]

if __name__ == '__main__':
	ss = "Jimmy has an apple, it is on the table, he like it"
	excludeWords = ["a", "an", "the"]
	s = Solution()
	print("小说的内容：", ss)
	print("统计不包含的单词：", excludeWords)
	print("最常出现的词：", s.frequentWord(ss, excludeWords))


# 运行结果
# 小说的内容： Jimmy has an apple, it is on the table, he like it
# 统计不包含的单词： ['a', 'an', 'the']
# 最常出现的词： it