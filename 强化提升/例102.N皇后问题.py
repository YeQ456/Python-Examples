# 问题描述
# 根据n皇后问题，返回n皇后不同解决方案的数量，而不是具体的放置布局


# 示例
# 输入：n = 4
# 输出：2
# 解释：方案1
# 0 0 1 0
# 1 0 0 0
# 0 0 0 1
# 0 1 0 0
#
# 方案2：
# 0 1 0 0 
# 0 0 0 1
# 1 0 0 0
# 0 0 1 0


# 源码实现
class Solution:
    total = 0
    n = 0
    def attack(self, row, col):
        for c, r in self.cols.items():
            if c - r == col - row or c + r == col + row:
                return True
            
    def search(self, row):
        if row == self.n:
            self.total += 1
            return
        for col in range(self.n):
            if col in self.cols:
                continue
            if self.attack(row, col):
                continue
            self.cols[col] = row
            self.search(row + 1)
            del self.cols[col]

    def totalNQueens(self, n):
        self.n = n
        self.cols = {}
        self.search(0)
        return self.total

# 主函数
if __name__ == '__main__':
    s = Solution()
    s.totalNQueens(4)
    print("Input: ", s.n)
    print("Output: ", s.total)



# 运行结果
# Input:  4
# Output:  2