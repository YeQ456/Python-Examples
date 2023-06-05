# 问题描述
# 非负数可以被视为其因数的乘积，编写一个函数来返回整数n的因数的所有可能组合。组合中的元素(a1,a2,...,ak)
# 必须是非降序，即a1 <= a2 <= ... <= ak。结果集中不能包含重复的组合


# 示例
# 输入：8
# 输出：[[2,2,2],[2,4]]
# 解释：8 = 2 x 2 x 2 = 2 x 4


# 源码实现
class Solution:
    def getFactors(self, n):
        result = []
        self.helper(result, [], n, 2)
        return result
    
    def helper(self, result, item, n, start):
        if n <= 1:
            if len(item) > 1:
                result.append(item[:])
            return
        import math
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                item.append(i)
                self.helper(result, item, n / i, i)
                item.pop()
        if n >= start:
            item.append(n)
            self.helper(result, item, 1, n)
            item.pop()

# 主函数
if __name__ == '__main__':
    nums = 8
    s = Solution()
    print("input: ", nums)
    print("output: ", s.getFactors(nums))


# 运行结果
# input:  8
# output:  [[2, 2, 2.0], [2, 4.0]]