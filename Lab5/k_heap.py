import math
import random

class KHeap:

    def __init__(self, values, k):
        self.data = values
        self.k = k
        self.length = len(values)
        self.build_heap(values)

    def build_heap(self, values):
        for i in range(self.length // self.k, -1, -1):
            self.sink(i)

    def parent(self, i):
        return (i + self.k - 1) // self.k - 1

    def children(self, i):
        childs = []
        for j in range(self.k):
            a = self.k*i + j + 1
            if a < self.length:
                childs.append(a)
        return childs

    def sink(self, i):
        largest_known = i
        for j in self.children(i):
            if j < self.length and self.data[j] > self.data[largest_known]:
                largest_known = j
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)
