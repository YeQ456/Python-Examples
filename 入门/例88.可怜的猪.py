# 问题描述
# 在1000个桶中仅有1个桶里装满了毒药，其他装的是水。这些桶从外面看上去完全相同。若一头猪喝了毒药，它将
# 在15分钟内死去。在1小时内，至少需要多少头猪才能判断出哪一个桶里装的是毒药？设计实现一个算法进行处理


# 示例
# 输入：buckets = 1000, minutesToDie = 15, minutesToTest = 60
# 输出：5
# 解释：一头猪在测试时间内有5种情况，15分钟时死亡，30分钟时死亡，45分钟时死亡，60分钟时死亡，60分钟时
# 存活，因此一头猪最多可以判断5桶水。两头猪最多可判断25桶水，将25桶水进行二维矩阵xy坐标编码，每行分别
# 混合，产生5桶水，一头猪求毒药的x坐标；同理每列分别混合产生5桶水，另一头猪求毒药的y坐标。同理可知,
# n头猪最多可以判断5^n桶水


# 源码实现 
class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while(minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs

# 主函数
if __name__ == '__main__':
    s = Solution()
    n = 1000
    m = 15
    p = 60
    print("Input: n = ", n, ", m = ", m, ", p = ", p)
    print("Output: ", s.poorPigs(n,m,p))



# 运行结果
# Input: n =  1000 , m =  15 , p =  60
# Output:  5