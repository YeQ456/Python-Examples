# 问题描述
# 假设你和n个人（标记为0 ~ n - 1）在聚会，其中可能存在一个名人。名人的定义是所有其他n - 1人都认识
# 他/她，但他/她不认识任何一个人。现在要验证这个名人不存在。唯一可以做的是提出问题“A,你认识B吗”，
# 获取A是否认识B。编写辅助函数bool know(a,b)确认A是否认识B; 编写函数int findCelebrity(n)实现
# 具体功能


# 示例
# 输入：2,0认识1,1不认识0
# 输出：1
# 解释：所有人认识1且1不认识其他人，所以1是名人

# 输入：3,0不认识1,0不认识2,1认识0,1不认识2,2认识0,2认识1
# 输出：-1
# 解释：没有名人


# 源码实现
class Celebrity:
    def knows(a, b):
        if a == 0 and b == 1:
            return True
        if a == 1 and b == 0:
            return False

class Solution:
    def findCelebrity(self, n):
        celeb = 0
        for i in range(1, n):
            if Celebrity.knows(celeb, i):
                celeb = i
        for i in range(n):
            if celeb != i and Celebrity.knows(celeb, i):
                return -1
            if celeb != i and not Celebrity.knows(i, celeb):
                return -1
        return celeb

# 主函数
if __name__ == '__main__':
    n = 2
    s = Solution()
    print("Input: ", n)
    print("Output: ", s.findCelebrity(n))


# 运行结果
# Input:  2
# Output:  1