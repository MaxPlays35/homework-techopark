import pprint
from collections import deque

n = int(input())

data = {i: [] for i in range(n)}
matrixAvailability = [[0 for j in range(n)] for i in range(n)]
stack = deque()

for i in range(n):
    vertices = list(map(int, input().split()))
    if vertices[0]:
        data[i].extend([(vertex - 1) for vertex in vertices])


print(data)
for k in range(n):
    stack.append(k)
    #matrixAvailability[k][k] = 1
    #print(stack)
    while stack:
        print(k,' ',stack)
        vertex = stack.popleft()
        #print(vertex)
        #print(k, ' ', stack)
        for i in data[vertex]:
            if matrixAvailability[k][i]:
                continue
            matrixAvailability[k][i] = 1
            test=data[vertex]
            for e in data[vertex]:
                if matrixAvailability[k][e] != 0:
                    stack.append(e)

pprint.pprint(matrixAvailability)

#pprint.pprint(data)
