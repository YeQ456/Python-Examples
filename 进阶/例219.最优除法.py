# 问题描述
# 给定一个正整数列表，对相邻的整数执行浮点数除法（如给定[2,3,4]，将其运算2/3/4）。在任意位置加入任意
# 数量的括号，以改变运算优先级。找出如何加括号能使结果最大，以字符串的形式返回表达式，且表达式不包括
# 多余的括号


# 示例
# 输入：[1000,100,10,2]
# 输出："1000/(100/10/2)"
# 解释：1000/(100/10/2) = 1000/((100/10)/2) = 200


# 源码实现
class Solution(object):
    def optimalDivision(self, nums):
        joinDivision = lambda l: '/'.join(list(map(str, l)))
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return joinDivision(nums)
        return str(nums[0]) if len(nums) == 1 else str(nums[0]) + '/(' + joinDivision(nums[1:]) + ')'

if __name__ == '__main__':
    nums = [1000,100,10,2]
    s = Solution()
    print("输入：", nums)
    print("输出：", s.optimalDivision(nums))


# 运行结果
# 输入： [1000, 100, 10, 2]
# 输出： 1000/(100/10/2)