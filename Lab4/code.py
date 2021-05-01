from lab4 import *
from sorts import *

import timeit
import math

def timetest_mergesort(n, alg1, alg2):
	L1_arr = []
	L2_arr = []
	for i in range(n):
		rand_list = create_random_list(i)
		L1_arr.append(rand_list)
		L2_arr.append(rand_list)

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

# timetest_mergesort(1000, mergesort, mergesort_bottom)
# timetest_mergesort(1000, mergesort, mergesort_three)
# timetest_mergesort(1000, merge_bottom, mergesort_three)


def timetest_worstcase(n, runs):
	L_arr = []
	factor = 0
	for _ in range(runs):
		L = near_sorted_list(n, factor)
		L_arr.append(L)
		factor += 0.5/runs

	for i in range(runs):
		start = timeit.default_timer()
		# merge sort best
		end = timeit.default_timer()
		diff = end - start

		print(i, diff)

# timetest_worstcase(1000, 1000)


a = create_random_list(1000)
print(a)
mergesort_three(a)
print(a)
