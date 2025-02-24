import sys

def bellman_ford(n, edges):
    dist = [float('inf')] * n
    dist[0] = 0

    for _ in range(n - 1):
        for x, y, t in edges:
            if dist[x] + t < dist[y]:
                dist[y] = dist[x] + t

    for x, y, t in edges:
        if dist[x] + t < dist[y]:
            return True

    return False

def main():
    c = int(sys.stdin.readline().strip())

    for _ in range(c):
        n, m = map(int, sys.stdin.readline().strip().split())
        edges = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

        print("possible" if bellman_ford(n, edges) else "not possible")

if __name__ == "__main__":
    main()