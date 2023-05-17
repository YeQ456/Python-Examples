# 问题描述
# 反转一个只有3位的整数

# 示例
# 输入：123
# 输出：321

# 输入：900
# 输出：9

# 源码实现
class Solution:
    def reverseInteger(self, number):
        a = int(number / 100)            # 百位数
        b = int(number % 100 / 10)       # 十位数
        c = int(number % 10)             # 个位数
        return(100 * c + 10 * b + a)     # 反转：个位数*100 + 十位数*10 + 百位数
 
# 主函数
if __name__ == '__main__':
    solution = Solution()
    num = 123
    ans = solution.reverseInteger(num)
    print("Input: ", num)
    print("Output: ", ans)


# 运行结果
# Input: 123
# Output: 321
