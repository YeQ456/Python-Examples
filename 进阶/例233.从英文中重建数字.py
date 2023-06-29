# 问题描述
# 给定一个非空字符串，包含用英文单词对应的数字0 - 9,但是字母顺序是打乱的，以升序输出数字


# 示例
# 输入："owoztneoer"
# 输出："012"（zeroonetwo）


# 源码实现
class Solution:
    def originalDitigs(self, s):
        nums = [0 for x in range(10)]
        nums[0] = s.count('z')
        nums[2] = s.count('w')
        nums[4] = s.count('u')
        nums[6] = s.count('x')
        nums[8] = s.count('g')
        nums[3] = s.count('h') - nums[8]
        nums[7] = s.count('s') - nums[6]
        nums[5] = s.count('v') - nums[7]
        nums[1] = s.count('o') - nums[0] - nums[2] - nums[4]
        nums[9] = (s.count('n') - nums[1] - nums[7]) // 2
        result = ""
        for x in range(10):
            result += str(x) * nums[x]
        return result

if __name__ == '__main__':
    s = Solution()
    n = "owoztneoer"
    print("输入：", n)
    print("输出：", s.originalDitigs(n))


# 运行结果
# 输入： owoztneoer
# 输出： 012