def minCoinNums(n):
    default = [0, 1, 2, 1, 2]
    if (n < 5):
        return default[n]
    else:
        return min(minCoinNums(n-1), minCoinNums(n-3), minCoinNums(n-5)) + 1
def minCoinNums(n):
    default = [0, 1, 2, 1, 2]
    if (n < 5):
        return default[n]
    else:
        i = 5 
        while(i <=n):
            tmp = min(default[i - 1], default[i - 3], default[i - 5]) + 1
            default.append(tmp)
            i += 1
        return default[-1]
if __name__ == '__main__':
    print(minCoinNums(20))
    