a = [1,2,4,7]
n = 4
k = 13

def dfs(i:int = 0, s:int = 0) -> bool:
    if i == n:
        return s == k

    if dfs(i+1, s):
        return True

    if dfs(i+1, s+a[i]):
        return True

    return False

if dfs():
    print("ok")

