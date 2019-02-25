def test(s, n):
    tmp = []
    if (n == int(s)):

    for i in range(1, len(s) + 1):
        tmp.append(i)
        test(s[i:],  n - int(s[:1]))
        