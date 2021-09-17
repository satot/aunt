garden = """
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
"""

def parse_garden(g):
    return [list(row) for row in g.split()]

def join_garden(g):
    return "\n".join(["".join(row) for row in g])

def dfs(g:list, x:int = 0, y:int = 0) :
    g[x][y] = "."

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= len(g) or ny >= len(g[x]):
                continue
            if g[nx][ny] == ".":
                continue
            dfs(g, nx, ny)
    return

count = 0
g = parse_garden(garden)

for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == "W":
            dfs(g, i, j)
            count += 1
        #print("*------------------------------------*")
        #print(join_garden(g))
        #print("*------------------------------------*")

print(count)
