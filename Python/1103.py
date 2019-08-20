class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i = 0
        res = [0 for i in range(num_people)]    
        while candies  > 0:
            if candies > i + 1:
                candies -= (i + 1)
                res[i % num_people] += (i + 1)
            else :
                res[i % num_people] += candies
                candies = 0
            i += 1
        return res