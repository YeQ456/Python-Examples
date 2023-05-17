# 问题描述
# 给定一个数组a[]，其中除了2个数，其他均出现2次，请找出不重复的2个数并返回


# 示例
# 输入：a = [1,2,5,5,6,6]
# 输出：[1,2]

# 输入：a = [3,2,7,5,5,7]
# 输出：[2,3]


# 源码实现
class Solution:
    def theTwoNumbers(self, a):
        ans = [0,0]
        for i in a:
            ans[0] = ans[0] ^ i
        
        t = 1
        while t & ans[0] != t:
            t = t << 1
        
        for i in a:
            if i & t == t:
                ans[1] = ans[1] ^ i
        
        ans[0] = ans[0] ^ ans[1]
        return ans

# 主函数
if __name__ == '__main__':
    arr = [1,2,5,1]
    solution = Solution()
    print("Input: arr = ", arr)
    print("Output: 两个不重复的数字：", solution.theTwoNumbers(arr))



# 运行结果
# Input: arr =  [1, 2, 5, 1]
# Output: 两个不重复的数字： [2, 5]