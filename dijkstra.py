vertices, start_global, end_global = map(int, input().split())

graph = {i + 1: {} for i in range(vertices)}

#  READ GRAPH
for i in range(vertices):
    pairs = input().split()
    for pair in pairs:
        temp = map(int, pair.split('-'))
        try:
            vertex, weight = temp
        except ValueError:
            continue
        graph[i + 1].update({
            vertex: weight
        })


def dijkstra(graph, start, end):
    d = [float('inf') for _ in range(vertices + 1)]
    used = [False for _ in range(vertices + 1)]
    d[start] = 0

    for vertex_1 in graph:
        v = None
        for vertex_2 in graph:
            if not used[vertex_2] and (v is None or d[vertex_2] < d[vertex_1]):
                v = vertex_2
        if d[v] == float('inf'):
            break
        for vertex_3 in graph[v]:
            if d[v] + graph[v][vertex_3] < d[vertex_3]:
                d[vertex_3] = d[v] + graph[v][vertex_3]

    return d[end]


def get_final_result(graph, start, end):
    distances = {dijkstra(graph, start, end), dijkstra(graph, end, start)}
    return min(distances) if min(distances) != float('inf') else 0


print(get_final_result(graph, start_global, end_global))
