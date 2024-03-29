# 问题描述
# 想知道一家公共停车场上午的最大化利润有多少。给定该停车场上午车辆入场时间与出场时间的记录表，写一个函数，计算出这家停车场
# 上午最多同时停放了多少辆车


# 示例
# 输入：a = [[8,9],[4,6],[3,7],[6,8]]
# 输出：2

# 输入：a = [[1,2],[2,3],[3,4],[4,5]]
# 输出：1


# 源码实现
class Solution:
	def getMax(self, a):
		ans = [0] * 23
		for i in a:
			for j in range(i[0], i[1]):
				ans[j] += 1
		max = ans[0]
		for i in ans:
			if i > max:
				max = i
		return max

if __name__ == '__main__':
	a = [[8,9],[4,6],[3,7],[6,8]]
	s = Solution()
	print("车辆进出表：", a)
	print("最多同时有：", s.getMax(a), "辆车")


# 运行结果
# 车辆进出表： [[8, 9], [4, 6], [3, 7], [6, 8]]
# 最多同时有： 2 辆车