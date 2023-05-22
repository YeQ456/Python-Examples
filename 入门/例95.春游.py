# 问题描述
# 有n组小朋友准备去春游，数组a表示每一组人数，保证每一组不超过4个人。现在有若干辆车，每辆车最多只能
# 坐4个人，同一组小朋友必须坐在同一辆车上，同时每辆车可以不坐满，问最少需要多少辆车才能满足小朋友们
# 的出行需求


# 示例
# 输入：a = [1,2,3,4],表示有4组，每组分别有1,2,3,4个小朋友
# 输出：3
# 解释：第1与第3组拼车，其他组各自组一辆车

# 输入：a = [1,2,2,2],表示有4组，每组分别有1,2,2,2个小朋友
# 输出：2
# 解释：第1与第2组拼车，第3与第4组拼车


# 源码实现
class Solution:
    def getAnswer(self, a):
        count = [0 for i in range(0,5)]
        for i in range(0,len(a)):
            count[a[i]] += 1
        count[1] -= count[3]
        if count[2] % 2 == 1:
            count[2] += 1
            count[1] -= 2
        res = count[4] + count[3] + count[2] / 2
        if count[1] > 0:
            res += count[1] / 4
            if not count[1] % 4 == 0:
                res += 1
        return int(res)
    
# 主函数
if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,4]
    print("Input: ", a)
    print("Output: ", s.getAnswer(a))



# 运行结果
# Input:  [1, 2, 3, 4]
# Output:  3