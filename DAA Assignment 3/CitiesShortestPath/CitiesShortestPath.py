V = 11
INF = 100000

def floydWarshall(M):
    dist = [[0 for i in range(V + 1)] for j in range(V + 1)]
    for i in range(V):
        for j in range(V):
            dist[i][j] = M[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    printSolution(dist)

def printSolution(dist):

    print("Shortest Distance from New York to Toronto is: ", dist[10][0], "units")
    print("Following matrix shows the shortest distances between all pairs of vertices : ")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % ('INF')),
            else:
                print("%7d\t" % (dist[i][j])),
            if j == V - 1:
                print("")


# creating the matrix manually
M = [[0, 70, 100, 180, INF, 104, INF, INF, INF, INF, INF],
     [70, 0, 65, INF, INF, INF, INF, INF, INF, INF, INF],
     [100, 65, 0, 60, INF, INF, INF, INF, INF, INF, INF],
     [180, INF, 60, 0, 70, INF, INF, INF, INF, INF, INF],
     [INF, INF, INF, 70, 0, 100, INF, 65, 70, INF, INF],
     [140, INF, 100, INF, INF, 0, 130, INF, INF, INF, INF],
     [INF, INF, INF, INF, INF, 130, 0, 160, INF, INF, INF],
     [INF, INF, INF, INF, 65, INF, 160, 0, INF, INF, 180],
     [INF, INF, INF, INF, 70, INF, INF, INF, 0, 60, INF],
     [INF, INF, INF, INF, INF, INF, INF, INF, 60, 0, 100],
     [INF, INF, INF, INF, INF, INF, INF, 180, INF, 100, 0]]

floydWarshall(M)
