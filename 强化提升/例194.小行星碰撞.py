# 问题描述
# 给定一个整数数组，代表小行星。对每颗小行星，绝对值表示其大小，符号表示其方向(正表示右，负表示左)。
# 每颗小行星以相同的速度移动
# 若两颗小行星相遇，则较小的小行星会爆炸。若两者的大小相同，则两者都会爆炸。沿同一方向移动的两颗
# 小行星永远不会相遇。返回所有碰撞发生后小行星的状态


# 示例
# 输入：[5,10,-5]
# 输出：[5,10]
# 解释：10和-5碰撞得10， 5和10永远不会碰撞

# 输入：[10,2,-5]
# 输出：[10]


# 源码实现
class Solution:
    def asteroidCollision(self, asteroids):
        ans, i, n = [], 0, len(asteroids)
        while i < n:
            if asteroids[i] > 0:
                ans.append(asteroids[i])
            elif len(ans) == 0 or ans[-1] < 0:
                ans.append(asteroids[i])
            elif ans[-1] <= -asteroids[i]:
                if ans[-1] < -asteroids[i]:
                    i -= 1
                ans.pop()
            i += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [5,10,-5]
    print("输入：", nums)
    print("输出：", s.asteroidCollision(nums))


# 运行结果
# 输入： [5, 10, -5]
# 输出： [5, 10]