n, s = map(int, input("Введите N и S через пробел: ").split())

matrix = []
for i in range(n):
    row = list(map(int, input("Вводи матрицу построчно: ").split()))
    matrix.append(row)

graph = [[] for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            graph[i+1].append(j+1)

visited = [False] * (n+1)
component = []

def dfs(v):
    visited[v] = True
    component.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(s)

print(f'Количество вершин: {len(component)}')
print("отсортированный список вершин " + ' '.join(map(str, sorted(component))))


'''
Введите N и S через пробел: 4 1
Вводи матрицу построчно: 0 0 1 0
Вводи матрицу построчно: 1 1 0 1
Вводи матрицу построчно: 1 1 1 1
Вводи матрицу построчно: 0 0 1 1
4
1 2 3 4
'''