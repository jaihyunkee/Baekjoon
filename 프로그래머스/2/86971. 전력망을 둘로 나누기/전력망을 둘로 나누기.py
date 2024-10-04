from collections import deque

dict_ = {}
def bfs(start, not_to_add):
    queue = deque()
    visited = set()
    res = 0
    queue.append(start)
    while queue:
        num = queue.popleft()
        visited.add(num)
        res += 1 
        for neighbor in dict_[num]:
            if neighbor not in visited and neighbor not in queue and neighbor != not_to_add:
                queue.append(neighbor)
    return res

def solution(n, wires):
    global dict_
    answer = 1000000
    for n in wires:
        f, t = n
        if f in dict_:
            dict_[f].append(t)
        else:
            dict_[f] = [t]
        if t in dict_:
            dict_[t].append(f)
        else:
            dict_[t] = [f]        
    print(dict_)
    # 한개씩 끊어보기
    for wire in wires:
        node_1 = wire[0]
        node_2 = wire[1]
        
        answer = min(answer, abs(bfs(node_1, node_2) - bfs(node_2, node_1)))
    
    return answer