import heapq

def dist(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

def find(node):
    if parents[node] == node:
        return node
    else:
        parents[node] = find(parents[node])
        return parents[node]
def union(node1, node2):
    # find the parent node and check if theirs are in same group
    root1, root2 = find(node1), find(node2)
    if root1 == root2:
        return True
    else:
        parents[root2] = root1
        return False

N, C = map(int, input().split())
points = []
parents = [i for i in range(N)]
pq = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

#find all edges connecting all nodes
for i in range(N):
    for j in range(1+i, N):
        a, b = points[i]
        c, d = points[j]
        cur = dist((a, b), (c, d))
        if cur >= C:
            heapq.heappush(pq, [cur, i, j])

total_cost = 0
num_edges = 0
while pq:
    cost, node1, node2 = heapq.heappop(pq)
    # if node1 and node2 are not in the same group connect them, add its cost and add 1 to num_edges
    if not union(node1, node2):
        total_cost += cost
        num_edges += 1
        if num_edges == (N-1):
            print(total_cost)

print(-1)

