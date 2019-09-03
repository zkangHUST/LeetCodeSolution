class Solution:
    def numUniqueEmails(self, emails):
        l = set()
        for email in emails:
            addr = self.check(email)
            if addr not in l:
                l.add(addr)
        return len(l)
    def check(self, s):
        addr = ""
        i = 0
        while i < len(s):
            if s[i] == '.':
                i += 1
                continue
            elif s[i] == '+':
                while i < len(s) and s[i] != '@':
                    i += 1
                break
            elif s[i] == '@':
                break
            else:
                addr += s[i]
                i += 1
        addr += s[i:]
        return addr

p = Solution()
# l = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
l = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
ans = p.numUniqueEmails(l)
