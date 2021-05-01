import disjoint_set
import min_heap

class WeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if not self.are_connected(node1, node2):
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)
        self.weights[(node1, node2)] = weight
        self.weights[(node2, node1)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)


def kruskal(G):
    MST = WeightedGraph()
    nodes = []
    for node in G.adj:
        MST.add_node(node)
        nodes.append(node)
    ds = disjoint_set.DisjointSet(nodes)
    Q = min_heap.MinHeap([])
    for node in G.adj:
        for neighbour in G.adj[node]:
            Q.insert(min_heap.Element((node, neighbour), G.w(node, neighbour)))
    print(ds)
    while not Q.is_empty():
        current_edge = Q.extract_min().value
        print("Considering edge: " + str(current_edge) + str(G.w(current_edge[0], current_edge[1])))
        if ds.find(current_edge[0]) != ds.find(current_edge[1]):
            MST.add_edge(current_edge[0], current_edge[1], G.w(current_edge[0], current_edge[1]))
            ds.union(current_edge[0], current_edge[1])
            print(ds)
    return MST










G = WeightedGraph()
G.add_node("a")
G.add_node("b")
G.add_node("c")
G.add_node("d")
G.add_node("e")
G.add_node("f")
G.add_node("g")

G.add_edge("a", "f", 2)
G.add_edge("a", "b", 2)
G.add_edge("a", "d", 7)
G.add_edge("b", "f", 5)
G.add_edge("b", "d", 4)
G.add_edge("b", "c", 1)
G.add_edge("b", "e", 3)
G.add_edge("c", "f", 4)
G.add_edge("c", "e", 4)
G.add_edge("d", "e", 1)
G.add_edge("d", "g", 5)
G.add_edge("e", "g", 7)












"""
def kruskal(G):
    MST = WeightedGraph()
    nodes = []
    for node in G.adj:
        MST.add_node(node)
        nodes.append(node)
    ds = disjoint_set.DisjointSet(nodes)
    Q = min_heap.MinHeap([])
    for node in G.adj:
        for neighbour in G.adj[node]:
            Q.insert(min_heap.Element((node, neighbour), G.w(node, neighbour)))
    print(ds)
    while not Q.is_empty():
        current_edge = Q.extract_min().value
        if ds.find(current_edge[0]) != ds.find(current_edge[1]):
            MST.add_edge(current_edge[0], current_edge[1], G.w(current_edge[0], current_edge[1]))
            ds.union(current_edge[0], current_edge[1])
            print(ds)
    return MST
"""