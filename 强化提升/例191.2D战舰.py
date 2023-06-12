# 问题描述
# 给一个2D甲板,统计有多少艘战舰，战舰用"X"表示，空地用"."表示。规则：战舰只能横向或者纵向放置，且战舰
# 大小只能是1 X N(1行N列)或N X 1(N行1列)。N可以是任意数。在两艘战舰之间至少有1个横向或纵向的格子
# 分隔，不能使战舰相邻


# 示例
# 输入：
# X . . X
# . . . X
# . . . X
# 输出：2，甲板上有两艘战舰


# 源码实现
class Solution(object):
    def countBattleships(self, board):
        len1 = len(board)
        if len1 == 0:
            return 0
        len2 = len(board[0])
        ans = 0
        for i in range(0, len1):
            for j in range(0, len2):
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') \
                    and (j == 0 or board[i][j - 1] == '.'):
                    ans += 1
        return ans

# 主函数
if __name__ == '__main__':
    s = Solution()
    nums = ["X..X","...X","...X"]
    print("输入：", nums)
    print("输出：", s.countBattleships(nums))


# 运行结果
# 输入： ['X..X', '...X', '...X']
# 输出： 2