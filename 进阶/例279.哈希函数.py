# 问题描述
# 数据结构中，哈希函数可用于将一个字符串(或任何其他类型)转化为小于哈希表大小且大于等于零的整数。一个好的哈希函数可以尽可能少
# 地产生冲突。一种广泛使用的哈希函数算法是使用数值33，假设任何字符串都是基于33的整数，给出一个字符串作为key和哈希表的大小，返回
# 这个字符串的哈希值


# 示例
# key = "abcd"，按照如下公式求哈希值，HASH_SIZE表示哈希表的大小
# hashcode("abcd") = (ascii(a) * 33³ + ascii(b) * 33² + ascii(c) * 33 + ascii(d)) % HASH_SIZE
# 				   = (97 * 33³ + 98 * 33² + 99 * 33 + 100) % HASH_SIZE
# 				   = 3595978 % HASH_SIZE
#
# 输入：key = "abcd", size = 10000
# 输出：978

# 输入：key = "abcd", size = 100
# 输出：78


# 源码实现
class Solution:
	def hashCode(self, key, HASH_SIZE):
		ans = 0
		for x in key:
			ans = (ans * 33 + ord(x)) % HASH_SIZE
		return ans

if __name__ == '__main__':
	num = 100
	key = "abcd"
	s = Solution()
	ans = s.hashCode(key, num)
	print("输入key: ", key)
	print("输入size: ", num)
	print("输出值：", ans)


# 运行结果
# 输入key:  abcd
# 输入size:  100
# 输出值： 78