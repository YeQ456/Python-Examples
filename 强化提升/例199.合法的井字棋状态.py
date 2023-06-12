# 问题描述
# 一个井字棋盘以字符串数组board的形式给出。board是一个3 * 3的数组，包含字符" "、"X"和"O"。
# 字符" "表示这一格是空的。井字棋游戏规则：玩家需要轮流在空格上放置字符。第1个玩家总是放置"X"字符，
# 第2个玩家放置"O"字符。"X"和"O"总是被放置在空格上，不能放置在已有字符的格子上; 当有3格相同的字符
# 占据一行、一列或者一条对角线的时候，游戏结束。当所有格子都非空时游戏也结束。游戏结束后不许再操作。
# 当且仅当在一个合法的井字棋游戏可以结束时，返回True


# 示例
# 输入：board = ["XOX"," X ", "   "]
# 输出：False


# 源码实现
class Solution:
    def validTicTacToe(self, board):
        num_X, num_O = 0, 0
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == 'X':
                    num_X += 1
                if board[i][j] == 'O':
                    num_O += 1
        if not (num_X == num_O or num_X == num_O + 1):
            return False
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == 'X':
                    return num_X == num_O + 1
                if board[i][0] == 'O':
                    return num_X == num_O
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j]:
                if board[0][j] == 'X':
                    return num_X == num_O + 1
                if board[0][j] == 'O':
                    return num_X == num_O
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                return num_X == num_O + 1
            if board[0][0] == 'O':
                return num_X == num_O
        if board[0][2] == board[1][1] == board[2][0]:
            if board[2][0] == 'X':
                return num_X == num_O + 1
            if board[2][0] == 'O':
                return num_X == num_O
        return True

if __name__ == '__main__':
    s = Solution()
    nums = ["O  ", "   ", "   "]
    print("输入：", nums)
    print("输出：", s.validTicTacToe(nums))


# 运行结果
# 输入： ['O  ', '   ', '   ']
# 输出： False