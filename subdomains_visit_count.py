# A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.
# For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq_domains = {}
        for domains_info in cpdomains:
            count, domains = domains_info.split(" ")
            count = int(count)
            domains = domains.split(".")
            cur_domain = ""
            for j in range(len(domains)):
                if cur_domain == "":
                    cur_domain = domains[len(domains)-j-1]
                else: 
                    cur_domain = domains[len(domains)-j-1] + "." + cur_domain
                if cur_domain in freq_domains:
                    freq_domains[cur_domain] += count
                else:
                    freq_domains[cur_domain] = count
        return [str(freq_domains[key]) + " " + key for key in freq_domains.keys()]
