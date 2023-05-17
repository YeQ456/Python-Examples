# 问题描述
# 给定一个包含若干个区间的List数组，长度为1000，例如[500,1500]、[2100,3100]。给定一个number，判断
# number是否在这些区间内，若在则返回True，否则返回False


# 示例
# 输入：List = [[100,1100],[1000,2000],[5500,6500]], number = 6000
# 输出：True
# 解释：6000在区间[5500,6500]内

# 输入：List = [[100,1100],[2000,3000]], number = 3500
# 输出：False


# 源码实现
class Solution:
    def isInterval(self, List, number):
        high = len(List) - 1
        low = 0
        while high >= low:
            if 0 < (number - List[(high + low) // 2][0]) <= 1000:
                return 'True'
            elif 1000 < number - List[(high + low) // 2][0]:
                low = (high + low) // 2 + 1
            elif 0 > number - List[(high + low) // 2][0]:
                high = (high + low) // 2 - 1
            
        return False

# 主函数
if __name__ == '__main__':
    number = 6000
    List = [[100,1100],[1000,2000],[5500,6500]]
    solution = Solution()
    print("Input: List = ", List, ", number = ", number)
    print("Output: ", solution.isInterval(List,number))



# 运行结果
# Input: List =  [[100, 1100], [1000, 2000], [5500, 6500]] , number =  6000
# Output:  True