from heap import Heap
from k_heap import KHeap

import math
import timeit
import random

# without duplicates
def create_random_list(n):
    L = []
    while len(L) < n:
        num = random.randint(1, n)
        if num not in L:
            L.append(num)
    return L

a = create_random_list(30)
heap = Heap(a)
heap.build_heap3()
print(heap)

def timetest_buildheap(n):
    
    L_arr = []
    
    for i in range(n):
        rand_list = create_random_list(i)
        L_arr.append(rand_list)

    for i in range(n):
        heap = Heap(L_arr[i])
        start = timeit.default_timer()
        #heap.build_heap1()
        #heap.build_heap2()
        heap.build_heap2()
        end = timeit.default_timer()
        diff = end - start

        print(diff)

#Run each heap.build_heap individually (total of 3 times) and then plot

# timetest_buildheap(1000)

#h = KHeap(create_random_list(20), 5)
#print(h.data)
