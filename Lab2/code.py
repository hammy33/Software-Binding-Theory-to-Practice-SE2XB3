import random
import math
import timeit

def copy(list1):
    list2 = list1.copy()
    return list2

def timetestfunction_copy(runs, n):
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        list1 = random.sample(range(1,1000), n)
        copy(list1)
        end = timeit.default_timer()
        total += end - start
    return total / runs

def timetestfunction_lookup(n):
    total = 0
    a_list = [0] * n
    for i in range(n):
        start = timeit.default_timer()
        temp = a_list[i] # lookup
        end = timeit.default_timer()
        diff = end - start
        total += diff
        print(i, diff)
    return "Average: " + str(total / n)

'''
IMPROVEMENTS
instead of printing out data for each lookup time, only
one data point is printed that take the average time for
the last div iterations.
'''
def timetestfunction_lookup2(n, div):
    total = 0
    oldtotal = 0
    a_list = [0] * n
    for i in range(n):
        j = random.randint(0, n-1)
        start = timeit.default_timer()
        temp = a_list[j] # lookup (random)
        end = timeit.default_timer()
        diff = end - start
        total += diff
        if i % div == 0 and i != 0:
            print(i, (total-oldtotal)/div)
            oldtotal = total
    return "Average: " + str(total / n)

def timetestfunction_append(n):
    total = 0
    a_list = []
    for i in range(n):
        start = timeit.default_timer()
        a_list.append(0)
        end = timeit.default_timer()
        diff = end - start
        total += diff
        print(i, diff)
    return "Average: " + str(total / n)

def timetestfunction_append2(n, div):
    total = 0
    oldtotal = 0
    a_list = []
    for i in range(n):
        start = timeit.default_timer()
        a_list.append(0) # lookup (random)
        end = timeit.default_timer()
        diff = end - start
        total += diff
        if i % div == 0 and i != 0:
            print(i, (total-oldtotal)/div)
            oldtotal = total
    return "Average: " + str(total / n)
    
def timetestfunction_extend(n, div):
    total = 0
    oldtotal = 0
    for i in range(n):
        a_list = []
        b_list = [0] * i
        start = timeit.default_timer()
        a_list.extend(b_list)
        end = timeit.default_timer()
        diff = end - start
        total += diff
        if i % div == 0 and i != 0:
            print(i, (total-oldtotal)/div)
            oldtotal = total

def main():

    # for i in range (1, 500):
    #     print(i, timetestfunction_copy(50, i))
    # print(timetestfunction_lookup(1000000))
    # print(timetestfunction_lookup2(1000000, 10000))
    # print(timetestfunction_append(1000000))
    #  print(timetestfunction_lookup2(1000000, 10000))
    # print(timetestfunction_extend(100000, 1000))