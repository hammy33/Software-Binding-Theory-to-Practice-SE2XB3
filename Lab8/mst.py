from lab8 import WeightedGraph
from min_heap import MinHeap, Element
import math


def prim1(G): # n^2
    # setup -- find least weighted edge in G
    MST = WeightedGraph(G.number_of_nodes())
    marked = [next(iter(G.adj))]

    for _ in range(G.number_of_nodes() - 1):
        min_node1, min_node2, min_w_edge = None, None, math.inf
        for node1 in marked:
            for node2, _ in G.adj[node1]:
                if node2 not in marked and G.w(node1, node2) < min_w_edge:
                    min_node1, min_node2, min_w_edge = node1, node2, G.w(node1, node2)
        MST.add_edge(min_node1, min_node2, min_w_edge)
        marked.append(min_node2)
    return MST


def prim2(G): # n log n
    MST = WeightedGraph(G.number_of_nodes())
    Q = MinHeap([])
    for node in G.adj:
        Q.insert(Element(node, math.inf))

    min_element = Q.extract_min()
    marked = [min_element.value]
    while not Q.is_empty(): # log n
        for node_adj, _ in G.adj[min_element.value]: # n
            if node_adj not in marked:
                Q.decrease_key(node_adj, G.w(min_element.value, node_adj))
        min_element = Q.extract_min()
        for node in marked: # n
            if min_element.key == G.w(node, min_element.value):
                MST.add_edge(node, min_element.value, min_element.key)
                break # reduce amt of comparisons
        marked.append(min_element.value)
    return MST


graph = WeightedGraph(7)

graph.add_edge(0, 5, 2)
graph.add_edge(0, 1, 2)
graph.add_edge(0, 3, 7)
graph.add_edge(1, 5, 5)
graph.add_edge(1, 3, 4)
graph.add_edge(1, 2, 1)
graph.add_edge(1, 4, 3)
graph.add_edge(2, 5, 4)
graph.add_edge(2, 4, 4)
graph.add_edge(3, 4, 1)
graph.add_edge(3, 6, 5)
graph.add_edge(4, 6, 7)

prim1graph = prim1(graph)
print(prim1graph.adj)

prim2graph = prim2(graph)
print(prim2graph.adj)
