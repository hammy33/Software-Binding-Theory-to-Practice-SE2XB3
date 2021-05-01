import random
# Merge helper function to merge two already sorted subarrays
def merge_bottom(L, start, mid, end):
 
    p1, p2, p3 = start, start, mid + 1
    temp = L.copy()
 
    # loop until no elements exist in left and right runs
    while p2 <= mid and p3 <= end:
        if L[p2] < L[p3]:
            temp[p1] = L[p2]
            p2 += 1
        else:
            temp[p1] = L[p3]
            p3 += 1
        p1 += 1
 
    # copy remaining elements
    while p2 < len(L) and p2 <= mid:
        temp[p1] = L[p2]
        p1 += 1
        p2 += 1
 
    # copy back to the original list
    for i in range(start, end + 1):
        L[i] = temp[i]
 
def mergesort_bottom(L):

    # divider will separate the list into different blocks with size "m"
    divider = 1
    while divider <= len(L) - 1:
        for i in range(0, len(L) - 1, 2 * divider):
            start = i
            mid = i + divider - 1
            end = min(i + 2*divider - 1, len(L) - 1)
            merge_bottom(L, start, mid, end)
        divider = 2 * divider


# Merge helper function to merge two already sorted subarrays
def merge_bottom(L, start, mid, end):
 
    p1, p2, p3 = start, start, mid + 1
    temp = L.copy()
 
    # loop until no elements exist in left and right runs
    while p2 <= mid and p3 <= end:
        if L[p2] < L[p3]:
            temp[p1] = L[p2]
            p2 += 1
        else:
            temp[p1] = L[p3]
            p3 += 1
        p1 += 1
 
    # copy remaining elements
    while p2 < len(L) and p2 <= mid:
        temp[p1] = L[p2]
        p1 += 1
        p2 += 1
 
    # copy back to the original list
    for i in range(start, end + 1):
        L[i] = temp[i]


def mergesort_bottom(L):
    # divider will separate the list into different blocks with size "m"
    divider = 1
    while divider <= len(L) - 1:
        for i in range(0, len(L) - 1, 2 * divider):
            start = i
            mid = i + divider - 1
            end = min(i + 2*divider - 1, len(L) - 1)
            merge_bottom(L, start, mid, end)
        divider = 2 * divider


def merge_three(left, center, right):
    L = []
    i = j = k = 0
    while i < len(left) or j < len(center) or k < len(right):
        if i >= len(left):
            if j >= len(center):
                L.append(right[k])
                k += 1
            elif k >= len(right):
                L.append(center[j])
                j += 1
            else:
                if center[j] <= right[k]:
                    L.append(center[j])
                    j += 1
                else:
                    L.append(right[k])
                    k += 1
        elif j >= len(center):
            if k >= len(right):
                L.append(left[i])
                i += 1
            else:
                if left[i] <= right[k]:
                    L.append(left[i])
                    i += 1
                else:
                    L.append(right[k])
                    k += 1
        elif k >= len(right):
            if left[i] <= center[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(center[j])
                j += 1
        # case where all sub arrays still have elements that need to be merged
        else:
            if left[i] <= center[j] and left[i] <= right[k]:
                L.append(left[i])
                i += 1
            elif center[j] <= left[i] and center[j] <= right[k]:
                L.append(center[j])
                j += 1
            else:
                L.append(right[k])
                k += 1
    return L


def mergesort_three(L):
    if len(L) == 2:
        divider = 1
    elif len(L) < 2:
	return
    else:
	divider = int((1/3)*len(L))
    left, center, right = L[:divider], L[divider: 2*divider], L[2*divider:]
    mergesort_three(left)
    mergesort_three(center)
    mergesort_three(right)
    temp = merge_three(left, center, right)

    for i in range(len(temp)):
        L[i] = temp[i]
