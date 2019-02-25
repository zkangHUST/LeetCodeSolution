class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        cnt = 0
        length = 0
        tmp = []
        while(i < len(chars)):
            m = chars[i]
            cnt = 0
            tmp.append(m)
            while(i < len(chars) and chars[i] == m):
                i += 1
                cnt += 1
            length += len(m)
            if (cnt > 1):
                tmp +=  list(str(cnt))
                length += len(str(cnt))
        chars[:] = tmp[:]
        return length


res = Solution()
# chars = ["a","a","b","b","c","c","c"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars =['a','a','a','a','a','a','a','a','a','a','a','a']
# chars = ["a"]
length = res.compress(chars)
print(chars)
print(length)
            
            