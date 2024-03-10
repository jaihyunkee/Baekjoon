from collections import defaultdict, deque

def bfs(k, v):
    count = 0
    visited = [False] * (len(videos) + 1)
    queue = deque()
    queue.append(v)
    visited[v] = True
    while len(queue) > 0:
        cur = queue.pop()
        for v in videos[cur]:
            cur_v = v[0]
            cur_usado = v[1]
            if not visited[cur_v] and cur_usado >= k:
                visited[cur_v] = True
                count += 1
                queue.append(cur_v)
    return count


N, Q = map(int, input().split())
videos = defaultdict(list)


for _ in range(N - 1):
    p, q, usado = map(int, input().split())
    videos[p].append((q,usado))
    videos[q].append((p,usado))

for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(k, v))