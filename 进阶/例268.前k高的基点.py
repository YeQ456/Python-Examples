# 问题描述
# 给定一个列表，列表中每个元素代表一位学生的学号StudentID和成绩GPA，返回GPA排名前K的学生的StudentID和GPA，按照原始数据的顺序输出


# 示例
# 输入：学生ID与成绩列表：[["001","4.53"],["002","4.87"],["003","4.99"]], K = 2
# 输出：[["002","4.87"],["003","4.99"]]


# 源码实现
from heapq import heappush, heappop
class Solution:
	def topKgpa(self, list, k):
		if len(list) == 0 or k < 0:
			return []
		minheap = []
		ID_set = set([])
		result = []
		for ID, GPA in list:
			ID_set.add(ID)
			heappush(minheap, (float(GPA), ID))
			if len(ID_set) > k:
				_, old_ID = heappop(minheap)
				ID_set.remove(old_ID)
		for ID, GPA in list:
			if ID in ID_set:
				result.append([ID, GPA])
		return result

if __name__ == '__main__':
	List = [['001','4.53'],['002','4.87'],['003','4.99']]
	k = 2
	s = Solution()
	print("学生按ID排序：", List, ", K = ", k)
	print("前K高GPA的学生：", s.topKgpa(List, k))


# 运行结果
# 学生按ID排序： [['001', '4.53'], ['002', '4.87'], ['003', '4.99']] , K =  2
# 前K高GPA的学生： [['002', '4.87'], ['003', '4.99']]