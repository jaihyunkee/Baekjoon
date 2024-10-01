import heapq

N = int(input())
M = int(input())

bus_routes = [tuple(map(int,input().split())) for _ in range(M)]

start, end = map(int, input().split())


all_routes = [(float("inf"), []) for _ in range(N + 1)]
routes = {}

pq = []
visited = [0 for _ in range(N + 1)]

for route in bus_routes:
    from_, to_, cost = route
    if from_ in routes.keys():
        routes[from_].append((cost, to_))
    else:
        routes[from_] = [(cost, to_)]

heapq.heappush(pq, (0, start))
all_routes[start] = (0, [start])
while pq:
    c, node = heapq.heappop(pq)
    if node == end:
        break
    if node in routes:
        for destination in routes[node]:
            c2, node2 = destination
            if all_routes[node][0] + c2 < all_routes[node2][0]:
                temp = list(all_routes[node][1])
                temp.append(node2)
                all_routes[node2] = (all_routes[node][0] + c2, temp)
                if visited[node2 - 1] == 0:
                    heapq.heappush(pq, (all_routes[node][0] + c2, node2))

print(all_routes[end][0])
print(len(all_routes[end][1]))
print(*all_routes[end][1])