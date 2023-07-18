# 问题描述
# 给定n瓶水，其中只有一瓶水是毒药，小白鼠会在喝下任何剂量的毒药后24小时死亡。请问若需要再24小时时知道哪瓶水是毒药，至少需要几只
# 小白鼠才能保证测试成功？


# 示例
# 输入：n = 3
# 输出：2

# 输入：n = 6
# 输出：3


#源码实现
class Solution:
	def getAns(self, n):
		n -= 1
		ans = 0
		while n != 0:
			n //= 2
			ans += 1
		return ans

if __name__ == '__main__':
	n = 4
	s = Solution()
	print("总共有：", n, "瓶水")
	print("至少需要：", s.getAns(n), "只小白鼠")


# 运行结果
# 总共有： 4 瓶水
# 至少需要： 2 只小白鼠