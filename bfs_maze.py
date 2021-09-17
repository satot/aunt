from queue import Queue

maze = """
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#....#
.####.###.
....#...G#
"""

# stack (in function) vs heap (global)
# a large size of data to be defined globally rather than defining inside
# function, in order not to store on stack but on heap

#INF = 1000000000
INF = "N"
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def deserialize(string:str):
    return [list(row) for row in string.split()]

def serialize(lst:list):
    return "\n".join([",".join([str(i) for i in row]) for row in lst])

def find_point(lst, target:str) -> tuple:
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == target:
                return (i, j)

def bfs(N, M, start, goal) -> int:
    q = Queue()
    d = [[INF for _ in range(M)] for _ in range(N)] # store distance
    (sx, sy) = start
    (gx, gy) = goal

    # starting point
    q.put((sx, sy))
    d[sx][sy] = 0

    while not q.empty():
        p = q.get()
        if p[0] == gx and p[1] == gy:
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if 0 <= nx and nx < N and 0 <= ny and ny < M and m[nx][ny] != "#" and d[nx][ny] == INF:
                q.put((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    print(maze)
    print(serialize(d))
    return d[gx][gy]


m = deserialize(maze)
start = find_point(m, "S")
goal  = find_point(m, "G")

print(bfs(len(m), len(m[0]), start, goal))
