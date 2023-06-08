# 问题描述
# 猜数游戏规则：从1~n选择一个数字，需要猜选择了哪个数字。每次猜错，程序会提示猜的数字是偏高还是偏低。
# 调用一个预定义的函数guess(int num)，程序会返回3个可能的结果(-1,1,0)，-1表示偏低，1表示偏高
# 0表示正确


# 示例
# 输入：n = 10, 选择了4,。
# 输出：4


# 源码实现
def guess(mid):
    if mid > 4:
        return -1
    if mid < 4:
        return 1
    if mid == 4:
        return 0

class Solution:
    def guessNumber(self, n):
        l = 1
        r = n
        while l <= r:
            mid = abs(1 + (r - l) / 2)
            res = guess(mid)
            if res == 0:
                return mid
            if res == -1:
                r = mid - 1
            if res == 1:
                l = mid + 1
        return int(mid)

# 主函数
if __name__ == '__main__':
    num = 10
    number = 4
    s = Solution()
    print("input: n = ", num, " selectNumber = ", number)
    print("output: ", s.guessNumber(num))


# 运行结果
# input: n = 10  selectNumber = 4
# output: 4