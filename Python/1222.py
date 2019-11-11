class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        return self.check(queens, king)
    
    def check(self, queens, king):
        res = []
        # L and R
        i , j = king[0], king[1]
        for j in range(king[1], -1, -1):
            if [i, j] in queens:
                res.append([i, j])
                break
        
        for j in range(king[1], 8):
            if [i, j] in queens:
                res.append([i, j])
                break
        # up and down 
        i , j = king[0], king[1]
        for i in range(king[0], -1, -1):
            if [i, j] in queens:
                res.append([i, j])
                break
        for i in range(king[0], 8):
            if [i, j] in queens:
                res.append([i, j])
                break
        
        #  /
        i, j = king[0], king[1]
        while i >= 0 and j < 8:
            if [i, j] in queens:
                res.append([i, j])
                break
            i -= 1
            j += 1
        
        i, j = king[0], king[1]
        while i < 8 and j >= 0:
            if [i, j] in queens:
                res.append([i, j])
                break
            i += 1
            j -= 1
        
        #  \
        i, j = king[0], king[1]
        while i >= 0 and j >= 0:
            if [i, j] in queens:
                res.append([i, j])
                break
            i -= 1
            j -= 1
        
        i, j = king[0], king[1]
        while i < 8 and j < 8:
            if [i, j] in queens:
                res.append([i, j])
                break
            i += 1
            j += 1

        return res