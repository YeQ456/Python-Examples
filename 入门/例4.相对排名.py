# 问题描述
# 根据N名运动员的得分，寻找相对等级和获得最高分前3名运动员，分别获得金牌、银牌和铜牌。其中N是正整数
# 所有运动员的成绩保证独一无二


# 示例
# 输入：[5,4,3,2,1]
# 输出：["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释：前3名运动员得分较高，根据得分依次获得金牌、银牌和铜牌。对于后两名运动员，根据分数输出相对
# 等级


# 数据要求
# 1 <= N <= 10000


# 源码实现
class Solution:
    def findRelativeRanks(self, nums):
        score = {}
        for i in range(len(nums)):
            score[nums[i]] = i;

        sortedScore = sorted(nums, reverse=True)
        answer = [0] * len(nums)

        for i in range(len(sortedScore)):
            res = str(i + 1)
            if i == 0:
                res = 'Gold Medal'
            if i == 1:
                res = 'Silver Medal'
            if i == 2:
                res = 'Bronze Medal'
            
            answer[score[sortedScore[i]]] = res
        
        return answer

#  主函数
if __name__ == '__main__':
    num = [5,4,3,2,1]
    solution = Solution()
    print("Input: ", num)
    print("Output: ", solution.findRelativeRanks(num))


# 运行结果
# Input:  [5, 4, 3, 2, 1]
# Output:  ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']