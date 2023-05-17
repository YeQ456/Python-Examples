# 问题描述
# 在x轴上分布着n个石子，用arr数组表示它们的位置。把这些石子移动到1,3,5,7,2n-1或者2,4,6,8,2n。
# 这些石子移动到1开始连续的奇数位，或从2开始连续的偶数位上，返回最少移动次数。每次只能移动1个
# 石子，只能把石子往左移动1个单位，同一个位置不能同时有2个石子


# 示例
# 输入：arr = [5,4,1]
# 输出：1
# 解释：只需要把4移动1步到3

# 输入：arr = [1,6,7,8,9]
# 输出：5
# 解释：把1移动到2，6移动到4,7移动到6,9移动到10


# 源码实现
class Solution:
    def moveStones(self, arr):
        arr = sorted(arr)
        even = 0
        odd = 0
        for i in range(0,len(arr)):
            odd += abs(arr[i] - (2 * i + 1))
            even += abs(arr[i] - (2 * i + 2))
        
        if odd < even:
            return odd

        return even

# 主函数
if __name__ == '__main__':
    arr = [1,6,7,8,9]
    solution = Solution()
    print("Input: arr = ", arr)
    print("Output: ", solution.moveStones(arr))



# 运行结果
# Input: arr =  [1, 6, 7, 8, 9]
# Output:  5