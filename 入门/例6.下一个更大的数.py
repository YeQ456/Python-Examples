# 问题描述
# 两个不重复的数组num1和num2，其中nums1是nums2的子集。在nums2的相应位置找到nums1所有元素的下一个
# 更大的数。
# 解释：nums1中的数字x的下一个更大数是nums2中x右边第1个更大的数字。如果不存在，则输出-1.


# 示例
# 输入：nums1 = [4,1,2], nums2 = [1,3,4,2]
# 输出：[-1,3,-1]
# 解释：nums1中第一个数字4在nums2中找不到比4大的第一个数字，所以返回-1；nums1中第二个数字1
# 在nums2中找到比1大的第一个数字3，所以返回3；以此类推......

# 输入：nums1 = [1,2,3], nuns2 = [1,4,2,5,3,6]
# 输出：[4,5,6]


# 数据要求
# nums1和nums2中的所有数字都是唯一
# 0 <= nums1 <= 1000
# 0 <= nums2 <= 1000


# 源码实现
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = {}
        stack = []
        for x in nums2:
            while stack and stack[-1] < x:
                ans[stack[-1]] = x
                del stack[-1]
            stack.append(x)
        
        for x in stack:
            ans[x] = -1
        
        return [ans[x] for x in nums1]

# 主函数
if __name__ == '__main__':
    solution = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print("Input: nums1 = ", nums1, ", nums2 = ", nums2)
    print("Output: ", solution.nextGreaterElement(nums1, nums2))



# 运行结果
# Input: nums1 =  [4, 1, 2] , nums2 =  [1, 3, 4, 2]
# Output:  [-1, 3, -1]