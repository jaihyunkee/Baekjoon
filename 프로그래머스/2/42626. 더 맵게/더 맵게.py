import heapq

def solution(scoville, K):
    # 힙 초기화
    heapq.heapify(scoville)
    ans = 0
    
    # 가장 작은 원소가 K 이상이 될 때까지 섞기
    while len(scoville) > 1:
        # 가장 작은 두 원소 꺼내기
        a = heapq.heappop(scoville)
        if a >= K:
            return ans
        b = heapq.heappop(scoville)
        
        # 새로운 스코빌 지수 생성
        new_sc = a + (b * 2)
        heapq.heappush(scoville, new_sc)
        ans += 1

    # 남은 하나의 스코빌 지수가 K 이상인지 체크
    if scoville[0] >= K:
        return ans
    else:
        return -1
