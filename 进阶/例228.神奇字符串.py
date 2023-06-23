# 问题描述
# 一个字符串S仅包含1和2，并遵守以下规则：
# 字符串S的前几个元素如下：S = "1221121221221121122..."。若将S中的连续1和2分组，它将是1 22 11 2 1 22
# 1 22 11 2 11 22 ... 并且每组中出现1或2的情况是1 2 2 1 1 2 1 2 2 1 2 2 ...。给定一个整数N作为输入，
# 返回神奇字符串S中前N个数字中的1的个数


# 示例
# 输入：6
# 输出：3
# 解释：字符串S的前6个元素是12211，包含3个1，所以返回3


# 源码实现
class Solution(object):
    def magicalString(self, n):
        if n == 0:
            return 0
        elif n <= 3:
            return 1
        else:
            so_far, grp, ones = [1,2,2], 2, 1
            while len(so_far) < n:
                freq, item = so_far[grp], 1 if grp % 2 == 0 else 2
                for _ in range(freq):
                    so_far.append(item)
                ones, grp = ones + freq if item == 1 else ones, grp + 1
            if len(so_far) == n:
                return ones
            else:
                return ones - 1 if so_far[-1] == 1 else ones

if __name__ == '__main__':
    s = Solution()
    n = 6
    print("输入：", n)
    print("输出：", s.magicalString(n))


# 运行结果
# 输入： 6
# 输出： 3