from mst import *
import random
import timeit

def create_random_complete_graph(n,upper):
	G = WeightedGraph()
	for i in range(n):
		G.add_node(i)
	randomb = 0
	for i in range(n):
		for j in range(n):
			if i != j:
				G.add_edge(i,j,random.randint(1,upper))
	return G

def timetest_prim_complete(n, upper, alg1, alg2):
	L1_arr = []
	L2_arr = []
	for i in range(n):
		random_graph = create_random_complete_graph(i+1, upper)
		L1_arr.append(random_graph)
		L2_arr.append(random_graph)
		
	for i in range(n):

		start = timeit.default_timer()
		alg1(L1_arr[i])
		end = timeit.default_timer()
		diff1 = end - start

		start = timeit.default_timer()
		alg2(L2_arr[i])
		end = timeit.default_timer()
		diff2 = end - start

		print(i, diff1, diff2)

timetest_prim_complete(100, 50, prim1, prim2)
