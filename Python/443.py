class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        while j < len(chars):
            ch = chars[j]
            cnt = 0
            while j < len(chars) and chars[j] == ch:
                cnt += 1
                j += 1
            chars[i] = ch
            i += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[i] = c
                    i += 1
        # print(chars[0:i])
        return i