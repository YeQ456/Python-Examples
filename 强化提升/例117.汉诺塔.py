# 问题描述
# 在A、B、C三根柱子上，有n个不同大小的圆盘，开始都叠在A上，目标是在最少的合法移动步数内将所有圆盘从
# A塔移动到C塔。游戏规则：每一步只允许移动1个圆盘，移动的过程中大圆盘不能在小圆盘上面


# 示例
# 输入：n = 2
# 输出：["from A to B","from A to C","from B to C"]

# 输入：n = 3
# 输出：["from A to C","from A to B","from C to B","from A to C","from B to A","from B to C","from A to C"]


# 源码实现
class Solution:
    def move(self, n, a, b, c, ans):
        if n == 1:
            ans.append("from " + a + " to " + c)
        else:
            self.move(n - 1, a, c, b, ans)
            ans.append("from " + a + " to " + c)
            self.move(n - 1, b, a, c, ans)
        return ans

# 主函数
if __name__ == '__main__':
    s = Solution()
    ans = []
    res = s.move(3, 'A', 'B', 'C', ans)
    print("Input: 3, 'A', 'B', 'C' ")
    print("Output: ", res)



# 运行结果
# Input: 3, 'A', 'B', 'C' 
# Output:  ['from A to C', 'from A to B', 'from C to B', 'from A to C', 'from B to A', 'from B to C', 'from A 
# to C']