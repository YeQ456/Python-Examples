# 问题描述
# 给定一个整数，返回起七进制的字符串表示


# 示例
# 输入：num = 100
# 输出：202

# 输入：num = -7
# 输出：-10


# 代码实现
class Solution:
    def convertToBase7(self, num):
        if num < 0:
            return '-' + self.convertToBase7(-num)
        if num < 7:
            return str(num)
        
        return self.convertToBase7(num // 7) + str(num % 7)

# 主函数
if __name__ == '__main__':
    num = 777
    solution = Solution()
    print("Input: num = ", num)
    print("Output: ", solution.convertToBase7(num))



# 运行结果
# Input: num =  777
# Output:  2160