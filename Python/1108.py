class Solution:
    def defangIPaddr(self, address: str) -> str:
        ret = ""
        for c in address:
            if c != '.':
                ret += c
            else:
                ret += "[.]"
        return ret