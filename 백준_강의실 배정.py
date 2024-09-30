import heapq

N = int(input())
classes = [list(map(int,input().split())) for _ in range(N)]
pq = []

for class_ in classes:
    heapq.heappush(pq, (class_[0], class_[1]))  # (start, end) 형태로 힙에 삽입

rooms = []

while pq:
    x,y = heapq.heappop(pq)
    if len(rooms) != 0:
        room = heapq.heappop(rooms)
        if room > x:
            heapq.heappush(rooms, room)
        heapq.heappush(rooms, y)


    else:
        heapq.heappush(rooms, y)
print(len(rooms))