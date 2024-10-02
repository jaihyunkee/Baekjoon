from collections import deque

def solution(bridge_length, weight, truck_weights):
    count = 0
    time = 0
    cur_w = 0
    cur = []
    while True:
        if count >= len(truck_weights) and not cur:
            return time
        
        to_remove = []
        for i in range(len(cur)):
            cur[i][0] -= 1
            if cur[i][0] == 0:
                to_remove.append(i)
                cur_w -= cur[i][1]
                
        for rm in to_remove:
            cur.pop(rm)

        
        if count < len(truck_weights):
            if cur_w + truck_weights[count] <= weight:
                cur.append([bridge_length, truck_weights[count]])
                cur_w += truck_weights[count]
                count += 1
        
        
        
        time += 1
        
    
    return time