# 问题描述
# 给每个孩子至多分1块饼干，每块饼干都有一个尺寸，同时每一个孩子都有一个贪吃指数，代表满足最小尺寸的饼干。
# 若饼干尺寸大于孩子的贪吃指数，则可以将饼干分给该孩子使他得到满足。目标是使最多的孩子得到满足，输出能
# 够满足孩子的最大值


# 示例
# 输入：孩子的贪吃指数[1,2,3], 饼干尺寸[1,1]
# 输出：1
# 解释：3个孩子的贪吃指数为1、2、3, 2块饼干的尺寸均为1，只有1个孩子得到满足


# 源码实现
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i

# 主函数
if __name__ == '__main__':
    s = Solution()
    n = [1,2,3]
    m = [1,1]
    print("Input: ", n, ", ", m)
    print("Output: ", s.findContentChildren(n,m))



# 运行结果
# Input:  [1, 2, 3] ,  [1, 1]
# Output:  1