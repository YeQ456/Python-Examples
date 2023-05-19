# 问题描述
# 给定一个整数矩阵，寻找一个最长递增路径。从每个单元格可以向上、下、左、右4个方向移动，不能沿着对角线
# 移动或移动到边界外，不许环绕


# 示例
# 输入：nums = [[9,9,4],[6,6,8],[2,1,1]]
# 输出：4
# 解释：最长递增路径：[1,2,6,9]


# 源码实现
DIRECTIONS = [(1,0),(-1,0),(0,-1),(0,1)]
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        sequence = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sequence.append((matrix[i][j], i, j))
        sequence.sort()
        check = {}
        for h, x, y in sequence:
            cur_pos = (x,y)
            if cur_pos not in check:
                check[cur_pos] = 1
            cur_path = 0
            for dx, dy in DIRECTIONS:
                if self.is_valid(x + dx, y + dy, matrix, h):
                    cur_path = max(cur_path, check[(x + dx, y + dy)])
            check[cur_pos] += cur_path
        vals = check.values()
        return max(vals)
    
    def is_valid(self, x, y, matrix, h):
        row, col = len(matrix), len(matrix[0])
        return x >= 0 and x < row and y >= 0 and y < col and matrix[x][y] < h

# 主函数
if __name__ == '__main__':
    solution = Solution()
    Test_in = [
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]
    Test_out = solution.longestIncreasingPath(Test_in)
    print("Input: ", Test_in)
    print("Output: ", Test_out)



# 运行结果
# Input:  [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
# Output:  4