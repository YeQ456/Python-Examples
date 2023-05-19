# 问题描述
# 给定整数a,b以及操作符+、-、*、/，然后得出简单计算结果


# 示例
# 输入：a = 1, b = 2, operator = +
# 输出：3

# 输入：a = 10, b = 20, operator = *
# 输出：200

# 输入：a = 3, b = 2, operator = /
# 输出：1

# 输入：a = 10, b = 11, operator = -
# 输出：-1


# 源码实现
class Solution:
    def calculate(self, a, operator, b):
        if operator == '+':
            return a + b
        
        if operator == '-':
            return a - b
        if operator == '*':
            return a * b
        if operator == '/':
            return a / b

# 主函数
if __name__ == '__main__':
    a = 8
    b = 3
    operator1 = '+'
    operator2 = '-'
    operator3 = '*'
    operator4 = '/'
    solution = Solution()
    print("Input: a = ", a, ", b = ", b, ", operator = ", operator1)
    print("Output: ", solution.calculate(a, operator1, b))
    print("Input: a = ", a, ", b = ", b, ", operator = ", operator2)
    print("Output: ", solution.calculate(a, operator2, b))
    print("Input: a = ", a, ", b = ", b, ", operator = ", operator3)
    print("Output: ", solution.calculate(a, operator3, b))
    print("Input: a = ", a, ", b = ", b, ", operator = ", operator4)
    print("Output: ", solution.calculate(a, operator4, b))



# 运行结果
# Input: a =  8 , b =  3 , operator =  +
# Output:  11
# Input: a =  8 , b =  3 , operator =  -
# Output:  5
# Input: a =  8 , b =  3 , operator =  *
# Output:  24
# Input: a =  8 , b =  3 , operator =  /
# Output:  2.6666666666666665