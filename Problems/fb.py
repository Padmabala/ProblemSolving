class Node:
    def __init__(self, vertex):
        self.element = vertex


class Graph:
    def __init__(self, graphSize):
        self.graphSize = graphSize
        self.vertices = []
        self.edges = []


T = int(input());
for i in range(T):
    N, Q = map(int, input().split()[:2])
    persons = list(input().split()[:N])
    query, nodes = input(), list(input.split()[:2])
    g = Graph(N)
    if (query == "addincircle")
