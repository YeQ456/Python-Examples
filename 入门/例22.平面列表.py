# 问题描述
# 给定一个列表，该列表中有的元素是列表，有的元素是整数。将其变成只包含整数的简单列表


# 示例
# 输入：[[1,1],2,[1,1]]
# 输出：[1,1,2,1,1]

# 输入：[1,2,[1,2]]
# 输出：[1,2,1,2]

# 输入：[4,[3,[2,[1]]]]
# 输出：[4,3,2,1]


# 源码实现
class Solution:
    def flatten(self, List):
        stack = [List]
        ans_list = []
        while stack:
            top = stack.pop()
            if isinstance(top, list):
                for elem in reversed(top):
                    stack.append(elem)
            else:
                ans_list.append(top)
        
        return ans_list

# 主函数
if __name__ == '__main__':
    solution = Solution()
    nums = [4,[3,[2,[1]]]]
    ans = solution.flatten(nums)
    print("Input: nums = ", nums)
    print("Output: ", ans)



# 运行结果
# Input: nums =  [4, [3, [2, [1]]]]
# Output:  [4, 3, 2, 1]