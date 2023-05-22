# 问题描述
# 给定一个字符串，找出它的所有排列，同一个字符串只能出现一次


# 示例
# 输入："abb"
# 输出：["abb","bab","bba"]

# 输入："aabb"
# 输出：["aabb","abab","baba","bbaa","abba","baab"]


# 源码实现
class Solution:
    def stringPermutation2(self, str):
        result = []
        if str == '':
            return ['']
        s = list(str)
        s.sort()
        while True:
            result.append(''.join(s))
            s = self.nextPermutation(s)
            if s is None:
                break
        return result
    
    def nextPermutation(self, num):
        n = len(num)
        i = n - 1
        while i >= 1 and num[i - 1] >= num[i]:
            i -= 1
        if i == 0:
            return None
        j = n - 1
        while j >= 0 and num[j] <= num[i - 1]:
            j -= 1
        num[i - 1], num[j] = num[j], num[i - 1]
        num[i:] = num[i:][::-1]
        return num

# 主函数
if __name__ == '__main__':
    s = Solution()
    str = "aabb"
    ans = s.stringPermutation2(str)
    print("Input: ", str)
    print("Output: ", ans)



# 运行结果
# Input:  aabb
# Output:  ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']