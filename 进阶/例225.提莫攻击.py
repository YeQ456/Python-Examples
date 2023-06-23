# 问题描述
# 在LOL中，有一个叫提莫的英雄，攻击能够让敌人艾希进入中毒状态。给定提莫的攻击时间点的升序序列，以及每次
# 提莫攻击时的中毒持续时间，输出艾希中毒状态的总时间。假设提莫在每一个具体的时间段一开始发起攻击，且
# 艾希立刻中毒；给定时间序列的长度不超过10000；提莫攻击的时间序列和中毒持续时间都是非负整数，不会
# 超过10000000


# 示例
# 输入：攻击时间序列[1,4]，中毒持续时间为2,
# 输出：4
# 解释：在第1秒开始，提莫攻击了艾希，艾希立刻中毒，这次中毒持续2秒，直到第2秒末尾。在第4秒开始，提莫
# 又开始攻击了艾希，让艾希中毒了2秒，所以最终结果为4

# 输入：攻击时间序列[1,2], 中毒持续时间为2
# 输出：3


# 源码实现
class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        ans = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i - 1]))
        return ans

if __name__ == '__main__':
    s = Solution()
    time = 2
    timws = [1,4]
    print("输入攻击序列：", timws)
    print("输入持续时间：", time)
    print("输出中毒时间：", s.findPoisonedDuration(timws, time))


# 运行结果
# 输入攻击序列： [1, 4]
# 输入持续时间： 2     
# 输出中毒时间： 4 