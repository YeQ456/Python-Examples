# 问题描述
# 判断是否可以利用所有火柴棍制作一个正方形。不破坏任何火柴棍，将它们连接起来，并且每个火柴棍必须使用一次。
# 输入火柴棍的长度，输出为真或假，表示是否可以制作一个正方形


# 示例
# 输入：[1,1,2,2,2]
# 输出：True
# 解释：用3个长度为2的火柴棍形成3个边，用两个长度为1的火柴棍形成第4条边，则能够成为正方形


# 源码实现
class Solution:
    def makesquare(self, nums):
        def dfs(nums, pos, target):
            if pos == len(nums):
                return True
            for i in range(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(nums, pos + 1, target):
                        return True
                    target[i] += nums[pos]
            return False
        
        if len(nums) < 4:
            return False
        numSum = sum(nums)
        nums.sort(reverse = True)
        if numSum % 4 != 0:
            return False
        target = [numSum / 4] * 4
        return dfs(nums, 0, target)

# 主函数
if __name__ == '__main__':
    s = Solution()
    n = [1,1,2,2,2]
    print("Input: ", n)
    print("Output: ", s.makesquare(n))



# 运行结果
# Input:  [1, 1, 2, 2, 2]
# Output:  True