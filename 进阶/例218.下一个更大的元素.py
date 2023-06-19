# 问题描述
# 给定一个32位整数n，用与n中相同的数字元素组成新的比n大的32位整数。返回符合要求的最小整数，若不存在这样
# 的整数，返回-1


# 示例
# 输入：123
# 输出：132


# 源码实现
class Solution:
    def nextGreaterElement(self, n):
        n_array = list(map(int, list(str(n))))
        if len(n_array) <= 1:
            return -1
        if len(n_array) == 2:
            if n_array[0] < n_array[1]:
                return int("".join(map(str, n_array[::-1])))
            else:
                return -1
        if n_array[-2] < n_array[-1]:
            n_array[-2], n_array[-1] = n_array[-1], n_array[-2]
            new_n = int("".join(map(str, n_array)))
        else:
            i = len(n_array) - 1
            while i > 0 and n_array[i - 1] >= n_array[i]:
                i -= 1
            if i == 0:
                return -1
            else:
                new_array = n_array[:i - 1]
                for j in range(len(n_array) - 1, i - 1, -1):
                    if n_array[j] > n_array[i - 1]:
                        break
                new_array.append(n_array[j])
                n_array[j] = n_array[i - 1]
                new_array.extend(reversed(n_array[i:]))
                new_n = int("".join(map(str, new_array)))
        return new_n if new_n <= 2 ** 31 else -1

if __name__ == '__main__':
    s = Solution()
    n = 123
    print("输入：", n)
    print("输出：", s.nextGreaterElement(n))


# 运行结果
# 输入： 123
# 输出： 132