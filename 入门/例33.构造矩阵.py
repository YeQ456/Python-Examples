# 问题描述
# 给定一个矩阵大小，设计其长(L)和宽(W)，并满足下面要求：矩形区域大小需要和给定目标相等；宽度W不大于
# 长度L，长和宽的差异尽可能小，并返回设计好的长度L和宽度W


# 示例
# 输入：4
# 输出：[2,2]
# 解释：目标面积为4，所有可能的组合为[1,4],[2,2],[4,1]。而[2,2]是最优解，即L = 2，W = 2


# 数据要求
# L >= W
# 1 <= L * W <= 10000000
# L和W都必须是正整数


# 源码实现
class Solution:
    def constructRectangle(self, area):
        import math
        W = math.floor(math.sqrt(area))
        while area % W != 0:
            W -= 1
        
        return [area // W, W]

# 主函数
if __name__ == '__main__':
    solution = Solution()
    area = 4
    print("Input: area =  ", area)
    print("Output: ", solution.constructRectangle(area))



# 运行结果
# Input: area =   4
# Output:  [2, 2]