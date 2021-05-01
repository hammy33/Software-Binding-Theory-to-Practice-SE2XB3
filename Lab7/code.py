from graphs import *
import random

def create_random_graph(n, m):
    edge_list = []
    G = Graph(n)
    for i in range(n):
        for j in range(i):
            edge_list.append((i, j))
    for _ in range(m):
        edge = random.choice(edge_list)
        G.add_edge(edge[0], edge[1])
        edge_list.remove(edge)
    return G


def test_has_cycle(n, k, c):
    for i in range(1, c+1):
        G_arr = []
        connected = 0
        not_connected = 0
        for j in range(n):
            G_arr.append(create_random_graph(k, i))
            if has_cycle(G_arr[j]):
                connected += 1
            else:
                not_connected += 1
        proportion = connected/not_connected
        print(i, proportion)


def test_is_connected(n, k, c):
    for i in range(k, k+c):
        G_arr = []
        connected = 0
        not_connected = 0
        for j in range(n):
            G_arr.append(create_random_graph(k, i))
            if is_connected(G_arr[j]):
                connected += 1
            else:
                not_connected += 1
        proportion = connected/(not_connected + 1)
        print(i, proportion)

# test_has_cycle(100, 100, 100)
# test_is_connected(100, 100, 1000)