def solution(citations):
    citations.sort()
    n = len(citations)
    if n == 1:
        if citations[0] == 0:
            return 0
        else:
            return 1

    for i in range(n):
        cur = n - i
        if citations[i] >= cur:
            return cur
    return 0
        
