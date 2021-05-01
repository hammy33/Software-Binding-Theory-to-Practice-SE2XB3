import random
import timeit
import math
from sorts import *

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L


def near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L
    

def timetest_inplace(n):
	L1_arr = []
	L2_arr = []
	total1 = 0
	total2 = 0
	for i in range(n):
		rand_list = create_random_list(i)
		L1_arr.append(rand_list)
		L2_arr.append(rand_list)
	
	for i in range(n):
		start1 = timeit.default_timer()
		my_quicksort(L1_arr[i])
		end1 = timeit.default_timer()
		diff1 = end1 - start1
		total1 += diff1

		start2 = timeit.default_timer()
		quicksort_inplace(L2_arr[i], 0, len(L2_arr[i])-1)
		end2 = timeit.default_timer()
		diff2 = end2 - start2
		total2 += diff2

		print(i, diff1, diff2)

# timetest_inplace(1000)


def timetest_multi_pivots(n):
    L1_arr = []
    L2_arr = []
    L3_arr = [] 
    L4_arr = []
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    for i in range(n):
        rand_list = create_random_list(i)
        L1_arr.append(rand_list)
        L2_arr.append(rand_list)
        L3_arr.append(rand_list)
        L4_arr.append(rand_list)

    for i in range(n):
        start1 = timeit.default_timer()
        dual_pivot_quicksort(L1_arr[i])
        end1 = timeit.default_timer()
        diff1 = end1 - start1
        total1 += diff1
        
        start2 = timeit.default_timer()
        tri_pivot_quicksort(L2_arr[i])
        end2 = timeit.default_timer()
        diff2 = end2 - start2
        total2 += diff2

        start3 = timeit.default_timer()
        quad_pivot_quicksort(L3_arr[i])
        end3 = timeit.default_timer()
        diff3 = end3 - start3
        total3 += diff3

        start4 = timeit.default_timer()
        quicksort_inplace(L4_arr[i])
        end4 = timeit.default_timer()
        diff4 = end4 - start4
        total4 += diff4

        print(i, diff1, diff2, diff3, diff4)


def timetest_small_lists(n):
    L1_arr = []
    L2_arr = []
    L3_arr = [] 
    L4_arr = []
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    for i in range(n):
        rand_list = create_random_list(i)
        L1_arr.append(rand_list)
        L2_arr.append(rand_list)
        L3_arr.append(rand_list)
        L4_arr.append(rand_list)

    for i in range(n):
        start1 = timeit.default_timer()
        quad_pivot_quicksort(L1_arr[i])
        end1 = timeit.default_timer()
        diff1 = end1 - start1
        total1 += diff1
        
        start2 = timeit.default_timer()
        bubble_sort(L2_arr[i])
        end2 = timeit.default_timer()
        diff2 = end2 - start2
        total2 += diff2

        start3 = timeit.default_timer()
        selection_sort(L3_arr[i])
        end3 = timeit.default_timer()
        diff3 = end3 - start3
        total3 += diff3

        start4 = timeit.default_timer()
        insertion_sort(L4_arr[i])
        end4 = timeit.default_timer()
        diff4 = end4 - start4
        total4 += diff4

        print(i, diff1, diff2, diff3, diff4)
	
# timetest_small_lists(500)


def timetest_quicksort_opt(n):
	L1_arr = []
	L2_arr = []
	L3_arr = []
	for i in range(n):
		rand_list = create_random_list(i)
		L1_arr.append(rand_list)
		L2_arr.append(rand_list)
		L3_arr.append(rand_list)

	for i in range(n):
		start1 = timeit.default_timer()
		quicksort_inplace(L1_arr[i], 0, len(L1_arr[i])-1)
		end1 = timeit.default_timer()
		diff1 = end1 - start1

		start2 = timeit.default_timer()
		final_sort(L2_arr[i], 0, len(L2_arr[i])-1)
		end2 = timeit.default_timer()
		diff2 = end2 - start2

		start3 = timeit.default_timer()
		insertion_sort(L3_arr[i])
		end3 = timeit.default_timer()
		diff3 = end3 - start3

		print(i, diff1, diff2, diff3)

# timetest_quicksort_opt(1000)


def time_all_sorts(n):
    L1_arr = []
    L2_arr = []
    L3_arr = [] 
    L4_arr = []
    for i in range(n):
        rand_list = near_sorted_list(n, i/n)
        L1_arr.append(rand_list)
        L2_arr.append(rand_list)
        L3_arr.append(rand_list)
        L4_arr.append(rand_list)
        
    for j in range(n):
        start1 = timeit.default_timer()
        bubble_sort(L1_arr[j])
        end1 = timeit.default_timer()
        diff1 = end1 - start1

        start2 = timeit.default_timer()
        selection_sort(L2_arr[j])
        end2 = timeit.default_timer()
        diff2 = end2 - start2

        start3 = timeit.default_timer()
        insertion_sort(L3_arr[j])
        end3 = timeit.default_timer()
        diff3 = end3 - start3

        start4 = timeit.default_timer()
        quad_pivot_quicksort(L4_arr[j])
        end4 = timeit.default_timer()
        diff4 = end4 - start4

        print (j, diff1, diff2, diff3)

# time_all_sorts(1000)


def timetest_worst_quicksort(n):
	L1_arr = []
	L2_arr = []
	for i in range(n):
		rand1_list = create_random_list(i)
		rand2_list = rand1_list
		rand2_list.sort()
		L1_arr.append(rand1_list)
		L2_arr.append(rand2_list)

	for i in range(n):
		start1 = timeit.default_timer()
		quicksort_inplace(L1_arr[i], 0, len(L1_arr[i])-1)
		end1 = timeit.default_timer()
		diff1 = end1 - start1

		start2 = timeit.default_timer()
		quicksort_inplace(L2_arr[i], 0, len(L2_arr[i])-1)
		end2 = timeit.default_timer()
		diff2 = end2 - start2

		print(i, diff1, diff2)

# timetest_worst_quicksort(1000)