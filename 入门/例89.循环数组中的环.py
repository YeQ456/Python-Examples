# 问题描述
# 一个数组包含正整数和负整数。若某个位置为正整数n，从这个位置出发正向(向右)移动n步；反之，若某个位置为
# 负整数-n，则从这个位置出发反向(向左)移动n步。数组被视为首尾相连，即第1个元素视为在最后一个元素右边
# 最后一个元素视为在第1个元素的左边。判断其中是否包含环，即从第一个确定的位置出发，在经过若干次移动后
# 仍能回到这个位置。环必须包含1个以上的元素，且必须是单向(不是正向就是反向)移动


# 示例
# 输入：[2,-1,1,2,2]
# 输出：True
# 解释：表示存在一个环，下标表示为：0->2->3->0


# 源码实现
class Solution:
    def get_index(self, i, nums):
        n = (i + nums[i]) % len(nums)
        return n if n >= 0 else n + len(nums)

    def circularArrayLoop(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            j, k = i, self.get_index(i, nums)
            while nums[k] * nums[i] > 0 and nums[self.get_index(k, nums)] * nums[i] > 0:
                if j == k:
                    if j == self.get_index(j, nums):
                        break
                    return True
                j = self.get_index(j, nums)
                k = self.get_index(self.get_index(k, nums), nums)
            j = i
            while nums[j] * nums[i] > 0:
                next = self.get_index(j, nums)
                nums[j] = 0
                j = next
        return False

# 主函数
if __name__ == '__main__':
    s = Solution()
    n = [2,-1,1,2,2]
    print("Input: ", n)
    print("Output: ", s.circularArrayLoop(n))



# 运行结果
# Input:  [2, -1, 1, 2, 2]
# Output:  True