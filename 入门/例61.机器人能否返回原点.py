# 问题描述
# 机器人位于坐标原点(0,0)处，给定一系列动作，判断该机器人的移动轨迹是否是一个环，即最终能否回到原来的
# 位置。移动的顺序由字符串表示，每个动作都由一个字符表示。有效的机器人移动是R(右)、L(左)、U(上)和D(下)。
# 输出为True或False，表示机器人是否回到原点


# 示例
# 输入：UD
# 输出：True
# 解释：上下各一次，回到原点


# 源码实现
class Solution:
    def judgeCircle(self, moves):
        count_RL = count_UD = 0
        for c in moves:
            if c == 'R':
                count_RL += 1
            if c == 'L':
                count_RL -= 1
            if c == 'U':
                count_UD += 1
            if c == 'D':
                count_UD -= 1
        
        return count_RL == 0 and count_UD == 0

# 主函数
if __name__ == '__main__':
    solution = Solution()
    moves = "UD"
    print("Input:", moves)
    print("Output:", solution.judgeCircle(moves))



# 运行结果
# Input: UD
# Output: True