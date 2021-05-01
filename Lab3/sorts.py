import math
import timeit
import random

def bubble_sort(L):
    for i in range(len(L)):
        swaps = 0
        for j in range(len(L)-i-1):
            if(L[j] > L[j+1]):
                swap(L, j, j+1)
                swaps += 1
        if swaps == 0:
            return


def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


def selection_sort(L):
    for i in range(len(L)-1): #optimize to only do L-1
        min_index = get_min_index(L, i) #we just want the remaining unsorter portion
        swap(L, i, min_index)


def get_min_index(L, n):
    min_index = n
    for i in range(n, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


def insertion_sort(L):
    for i in range(1, len(L)): #first element is sorted, nothing to insert_into
        insert_into(L, i)


def insert_into(L, n):
    i = n
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i, i-1)
        else: #done sorting
            return
        i -= 1


def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# Reference of inplace quicksort: https://www.geeksforgeeks.org/quick-sort/


def quicksort_inplace_partition(a, low, high):
	i = low - 1
	pivot = a[high]
	for j in range(low, high):
		if a[j] < pivot:
			i += 1
			a[i], a[j] = a[j], a[i] # swap
	a[i+1], a[high] = a[high], a[i+1]
	return i + 1 # index of sorted element


def quicksort_inplace(a, low, high):
	if low < high:
		pi = quicksort_inplace_partition(a, low, high) # pi is already sorted
		quicksort_inplace(a, low, pi-1)
		quicksort_inplace(a, pi+1, high)


def dual_pivot_quicksort(array):
    if len(array) <= 1:
        return array
    elif len(array) == 2:
        return sorted(array)
    pivot1, pivot2 = sorted([array.pop(0), array.pop(0)])
    a = []
    b = []
    c = []
    for i in array:
        if i < pivot1:
            a.append(i)
        elif pivot1 <= i < pivot2:
            b.append(i)
        else:
            c.append(i)
    return dual_pivot_quicksort(a) + [pivot1] + dual_pivot_quicksort(b) + [pivot2] + dual_pivot_quicksort(c) 


def tri_pivot_quicksort(array):
    if len(array) <= 1:
        return array
    elif len(array) == 2:
        return sorted(array)
    pivot1, pivot2, pivot3 = sorted([array.pop(0), array.pop(0), array.pop(0)])
    a = []
    b = []
    c = []
    d = []
    for i in array:
        if i < pivot1:
            a.append(i)
        elif pivot1 <= i < pivot2:
            b.append(i)
        elif pivot2 <= i < pivot3:
            c.append(i)
        else:
            d.append(i)
    return tri_pivot_quicksort(a) + [pivot1] + tri_pivot_quicksort(b) + [pivot2] + tri_pivot_quicksort(c) + [pivot3] + tri_pivot_quicksort(d)  


def quad_pivot_quicksort(array):
    if len(array) <= 1:
        return array
    elif len(array) == 2 or len(array) == 3:
        return sorted(array)
    pivot1, pivot2, pivot3, pivot4 = sorted([array.pop(0), array.pop(0), array.pop(0), array.pop(0)])
    a = []
    b = []
    c = []
    d = []
    e = []
    for i in array:
        if i < pivot1:
            a.append(i)
        elif pivot1 <= i < pivot2:
            b.append(i)
        elif pivot2 <= i < pivot3:
            c.append(i)
        elif pivot3 <= i < pivot4:
            d.append(i)
        else:
            e.append(i)
    return quad_pivot_quicksort(a) + [pivot1] + quad_pivot_quicksort(b) + [pivot2] + quad_pivot_quicksort(c) + [pivot3] + quad_pivot_quicksort(d) + [pivot4] + quad_pivot_quicksort(e)


def insert_sort(a, low, n):
    for i in range(low+1, n+1):
        val = a[i]
        j = i
        while j > low and a[j-1] > val:
            a[j] = a[j-1]
            j -= 1
        a[j] = val


def quicksort_partition(a, low, high):
    pivot = a[high]
    i = low
    j = low
    for i in range(low, high):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[j], a[high] = a[high], a[j]
    return j


def final_sort(a, low, high):
    while low < high:
        if high - low + 1 < 10:
            insert_sort(a, low, high)
            break
        else:
            pivot = quicksort_partition(a, low, high)
            if pivot - low < high - pivot:
                final_sort(a, low, pivot-1)
                low = pivot + 1
            else:
                final_sort(a, pivot+1, high)
                high = pivot - 1