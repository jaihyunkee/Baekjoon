from collections import deque

def solution(priorities, location):
    copy = priorities.copy()
    copy.sort(reverse=True)
    queue = deque()
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
    
    count = 0
    while queue:
        idx, prio = queue.popleft()
        print(idx, prio)
        if copy[count] == prio:
            count += 1
            if idx == location:
                return count
            continue
        else:
            queue.append((idx, prio))
    
            
        
        
    answer = 0
    return answer