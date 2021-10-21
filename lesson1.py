import pprint

vertices = int(input())

matrix = {i: [*[0]*vertices] for i in range(vertices)}
matrixAvailability = [[0 for j in range(vertices)] for i in range(vertices)]
visited = []

for i in range(vertices):
    array = list(map(int, input().split()))
    for vertex in range(0, len(array), 2):
        matrix[i][array[vertex]] = array[vertex + 1]

gen_list = [10 ** 10 for i in range(vertices)]
gen_list[0] = 0
for vertex in range(vertices):
    minimum = 10 ** 10
    min_idx = -1
    for elem in range(vertices):
        if minimum > gen_list[elem] and elem not in visited:
            min_idx = elem
            minimum = gen_list[elem]
            visited.append(elem)

    for i in range(vertices):
        if matrix[min_idx][i]:
            gen_list[i] = matrix[min_idx][i]

    print(minimum)

print(gen_list)


pprint.pprint(matrix)
pprint.pprint(matrixAvailability)
