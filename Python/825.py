class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = 0
        for i in range(len(ages)):
            for j in range(len(ages)):
                if i == j:
                    
            cnt += self.get(ages, i)
        return cnt
    def get(self, ages, m):
        cnt = 0
        for i in range(len(ages)):
            for 
            if i == m:
                continue
            if self.check(ages[m], ages[i]):
                cnt += 1
        return cnt
    def check(self, m, n):
        if n <= 0.5 * m + 7:
            return False
        if n > m:
            return False
        if n > 100 and m < 100:
            return False
        return True
