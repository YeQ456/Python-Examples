# 问题描述
# 在一个森林中，每个兔子都有一种颜色。兔子中的一部分（也可能是全部）会告诉你有多少兔子和它们有同样
# 的颜色。这些答案被放在了一个数组中。返回森林中兔子可能的最少数量


# 示例
# 输入：[1,1,2]
# 输出：5
# 解释：两个回答"1"的兔子可能是相同的颜色，定为红；回答"2"的兔子不一定是红色，定为蓝，一定还有
# 2只蓝色的兔子在森林但没有回答问题，则森林里兔子最少总数为5


# 源码实现
import math
class Solution:
    def numRabbits(self, answers):
        hash = {}
        for i in answers:
            if i + 1 in hash:
                hash[i + 1] += 1
            else:
                hash[i + 1] = 1
        ans = 0
        for i in hash:
            ans += math.ceil(hash[i] / i) * i
        return ans

if __name__ == '__main__':
    s = Solution()
    num = [1,1,2]
    print("输入：", num)
    print("输出：", s.numRabbits(num))


# 运行结果
# 输入： [1, 1, 2]
# 输出： 5