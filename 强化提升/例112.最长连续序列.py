# 问题描述
# 给定一个未排序的整数数组，找出最长连续序列的长度


# 示例
# 输入：[100,4,200,1,3,2]
# 输出：4
# 解释：最长的连续序列为[1,2,3,4]，则返回其长度4


# 源码实现
class Solution:
    def longestConsecutive(self, num):
        dict = {}
        for x in num:
            dict[x] = 1
        ans = 0
        for x in num:
            if x in dict:
                len = 1
                del dict[x]
                l = x - 1
                r = x + 1
                while l in dict:
                    del dict[l]
                    l -= 1
                    len += 1
                while r in dict:
                    del dict[r]
                    r += 1
                    len += 1
                if ans < len:
                    ans = len
        return ans

# 主函数
if __name__ == '__main__':
    s = Solution()
    num = [100, 4, 200, 1, 3, 2]
    ans = s.longestConsecutive(num)
    print("Input: ", num)
    print("Output: ", ans)



# 运行结果
# Input:  [100, 4, 200, 1, 3, 2]
# Output:  4