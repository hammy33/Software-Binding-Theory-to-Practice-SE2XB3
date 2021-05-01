from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS2(G, node1, node2):
    L = []
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        for i in range(G.number_of_nodes()):
            if len(G.adj[i]) != 0:
                continue
            return L
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        L.append(current_node)
        for node in G.adj[current_node]:
            if node == node2:
                L.append(node2)
                return L
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return []


#Depth First Search
def DFS2(G, node1, node2):
    L = []
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    for node in G.adj:
        for i in range(G.number_of_nodes()):
            if len(G.adj[i]) != 0:
                continue
            return L
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            L.append(current_node)
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    L.append(node2)
                    return L
                S.append(node)
    return []


def BFS3(G, init_node):
    Q = deque([init_node])
    visited_nodes = [init_node]
    pred_dict = {}

    while len(Q) != 0:
        current_node = Q.popleft()
        for adj_node in G.adj[current_node]:
            if adj_node not in visited_nodes:
                Q.append(adj_node)
                pred_dict[adj_node] = current_node
                visited_nodes.append(adj_node)
    return pred_dict


def DFS3(G, init_node):
    S = [init_node]
    visited_nodes = [init_node]
    pred_dict = {}

    while len(S) != 0:
        if all(adj_node in visited_nodes for adj_node in G.adj[S[-1]]):
            S.pop()
        else:
            current_node = S[-1]
            for adj_node in G.adj[current_node]:
                if adj_node not in visited_nodes:
                    S.append(adj_node)
                    pred_dict[adj_node] = current_node
                    visited_nodes.append(adj_node)
                    break
    return pred_dict


def is_connected(G):
    for i in range(G.number_of_nodes()):
        for j in range(G.number_of_nodes()):
            if i != j:
                if len(BFS2(G, i, j)) == 0:
                    return False
        return True
    

def has_cycle(G):
    checked = [False] * G.number_of_nodes()
    for a in range(G.number_of_nodes()):
        if checked[a] != True:
            if (has_cycle_rec(G, a, checked, -1)) == True:
                return True
        else:
            return False


def has_cycle_rec(G, g, checked, prev):
    checked[g] = True
    for a in G.adj[g]:
        if checked[a] != True:
            if (has_cycle_rec(G, a, checked, g)):
                return True
        elif prev != a:
            return True
        else:
            return False


# graph = Graph(10)
# graph.add_edge(0, 1)
# graph.add_edge(0, 4)
# graph.add_edge(0, 7)
# graph.add_edge(1, 2)
# graph.add_edge(2, 3)
# graph.add_edge(4, 5)
# graph.add_edge(5, 6)
# graph.add_edge(7, 8)
# graph.add_edge(8, 9)
# print(graph.adj)
# print(DFS2(graph, 0, 9))

# graph = Graph(4)
# graph.add_edge(0, 1)
# graph.add_edge(1, 0)
# print(has_cycle(graph))
# print(is_connected(graph))