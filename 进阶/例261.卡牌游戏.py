# 问题描述
# 在卡牌游戏中，一共有n张牌，每张牌的成本为cost[i]，可造成damage[i]的伤害。一共有totalMoney元，并需要造成至少totalDamage的
# 伤害才能获胜。每张牌只能使用一次，判断是否可以取得胜利


# 示例
# 输入：cost = [3,4,5,1,2], damage = [3,5,5,2,4], totalMoney = 7, totalDamage = 11
# 输出：True


# 源码实现
class Solution:
	def cardGame(self, cost, damage, totalMoney, totalDamage):
		num = len(cost)
		dp = [0] * (totalMoney + 1)
		for i in range(0, num):
			for j in range(totalMoney, cost[i] - 1, -1):
				dp[j] = max(dp[j], dp[j - cost[i]] + damage[i])
				if dp[j] >= totalDamage:
					return True
		return False

if __name__ == '__main__':
	cost = [3,4,5,1,2]
	damage = [3,5,5,2,4]
	totalMoney = 7
	totalDamage = 11
	s = Solution()
	print("卡牌的cost和damage分别为：", cost, damage)
	print("总共拥有金钱：", totalMoney)
	print("需要造成的伤害：", totalDamage)
	print("是否达成：", s.cardGame(cost, damage, totalMoney, totalDamage))


# 运行结果
# 卡牌的cost和damage分别为： [3, 4, 5, 1, 2] [3, 5, 5, 2, 4]
# 总共拥有金钱： 7
# 需要造成的伤害： 11
# 是否达成： True