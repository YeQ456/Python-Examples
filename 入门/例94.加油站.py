# 问题描述
# 汽车在一条道路上行驶，开始有original单位的汽油。这条道路上有n个加油站，第i个加油站距离汽车出发位置
# 的距离为distance[i]单位距离，可以给汽车加apply[i]单位汽油。汽车每行驶1单位距离会消耗1单位的汽油。
# 假设汽车的油箱可以装无限多的汽油，目的地距离汽车出发位置的距离为target，问汽车能否到达目的地，若
# 可以，返回最少的加油次数，否则返回-1 


# 示例
# 输入：target = 25, original = 10, distance = [10,14,20,21], apply = [10,5,2,4]
# 输出：2
# 解释：需要在第1个和第2个加油站加油

# 输入：target = 25, original = 10, distance = [10,14,20,21], apply = [1,1,1,1]
# 输出：-1
# 解释：汽车无法到达目的地


# 源码实现
class Solution:
    def getTimes(self, target, original, distance, apply):
        import queue
        que = queue.PriorityQueue()
        ans, pre = 0, 0
        if(target > distance[len(distance) - 1]):
            distance.append(target)
            apply.append(0)
        cap = original
        for i in range(len(distance)):
            if(distance[i] >= target):
                distance[i] = target
            d = distance[i] - pre
            while(cap < d and que.qsize() != 0):
                cap += (que.get()[1])
                ans += 1
            if(d <= cap):
                cap -= d
            else:
                ans = -1
                break
            que.put((-apply[i],apply[i]))
            pre = distance[i]
            if(pre == target):
                break
        return ans

#主函数
if __name__ == '__main__':
    target = 25
    original = 10
    distance = [10,14,20,21]
    apply = [10,5,2,4]
    s = Solution()
    print("Input: target = ", target, ", original = ", original, ", distance = ", distance, ", apply = ", apply)
    print("Output: ", s.getTimes(target,original,distance,apply))



# 运行结果
# Input: target =  25 , original =  10 , distance =  [10, 14, 20, 21] , apply =  [10, 5, 2, 4]
# Output:  2