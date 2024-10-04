def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    mst = set()
    mst.add(costs[0][0])
    ans = 0
    while len(mst) != n:
        for v in costs:
            if v[0] in mst and v[1] in mst:
                continue
            elif v[0] in mst or v[1] in mst:
                mst.add(v[0])
                mst.add(v[1])
                ans += v[2]
                break
                    
    return ans