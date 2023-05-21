# 问题描述
# 给一个整数c，判断是否存在两个整数a和b，使得a² + b² = c


# 示例
# 输入：n = 5
# 输出：True
# 解释：1² + 2² = 5


# 源码实现
import math
class Solution:
    def checkSumOfSquareNumbers(self, num):
        if num < 0:
            return False
        for i in reversed(range(0, int(math.sqrt(num)) + 1)):
            if i * i == num:
                return True
            j = num - i * i
            k = int(math.sqrt(j))
            if k * k == j:
                return True
        
        return False

# 主函数
if __name__ == '__main__':
    solution = Solution()
    num = 5
    print("Input: num = ", num)
    print("Output: ", solution.checkSumOfSquareNumbers(num))



# 运行结果
# Input: num =  5
# Output:  True