# 问题描述
# 两个管子，容量分别为x和y升。可以获取到无限数量的水，判断能否使用这两个罐子量出恰好z升的水（即在若干次
# 操作后，可以在一个或两个罐子中盛上z升的水）。允许的操作：将任意一罐子盛满水；倒空任意一罐罐子里的水；
# 将一个罐子中的水倒入另一个罐子，直到这个罐子完全空或另一个罐子完全满。


# 示例
# 输入：x = 3, y = 5, z = 4
# 输出：True
# 解释：可用公式：z = m * x + n * y，其中m、n为舀水和倒水的次数，正数位往里舀水，负数为往外舀水
# 则，4 = (-2) * 3 + 2 * 5


# 源码实现
class Solution:
    def canMeasureWater(self, x, y, z):
        if x + y < z:
            return False
        return z % self.gcd(x,y) == 0
    
    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x % y)
    
if __name__ == '__main__':
    s = Solution()
    x = 3
    y = 5
    z = 4
    print("输入x = ", x)
    print("输入y = ", y)
    print("输入z = ", z)
    print("输出：", s.canMeasureWater(x,y,z))


# 运行结果
# 输入x =  3
# 输入y =  5
# 输入z =  4
# 输出： True