# 问题描述
# 诸如school.bupt.edu这样的域名由各种子域名构成。最顶层是edu，下一层是bupt.edu，最底层是
# school.bupt.edu。当访问该域名时，会隐式访问子域名bupt.edu和edu。给出域名的访问计数格式为
# “计数 地址”，给出计数表，返回每个子域名(包含父域名)的访问次数(与输入格式相同，顺序随机)


# 示例
# 输入：["9001 school.bupt.edu"]
# 输出：["9001 school.bupt.edu", "9001 bupt.edu", "9001 edu"]
# 解释：只有一个域名："school.bupt.edu"，如题所述，子域名"bupt.edu"和"edu"也会被访问，所以
# 需要访问9001次


# 源码实现
class Solution:
    def subdomainVisits(self, cpdomains):
        # 利用哈希表对子域名计数，对字符串进行划分
        count = {}
        for domain in cpdomains:
            visits = int(domain.split()[0])
            domain_segments = domain.split()[1].split('.')
            top_level_domain = domain_segments[-1]
            sec_level_domain = domain_segments[-2] + '.' + domain_segments[-1]
            count[top_level_domain] = count[top_level_domain] + visits if top_level_domain in count.keys() else visits
            count[sec_level_domain] = count[sec_level_domain] + visits if sec_level_domain in count.keys() else visits
            if domain.count('.') == 2:
                count[domain.split()[1]] = count[domain.split()[1]] + visits if domain.split()[1] in count.keys() else visits
            
        return [str(v) + ' ' + k for k, v in count.items()]

# 主函数
if __name__ == '__main__':
    solution = Solution()
    inputnum = ["1201 school.bupt.edu"]
    print("Input: ", inputnum)
    print("Output: ", solution.subdomainVisits(inputnum))



# 运行结果
# Input:  ['1201 school.bupt.edu']
# Output:  ['1201 edu', '1201 bupt.edu', '1201 school.bupt.edu']