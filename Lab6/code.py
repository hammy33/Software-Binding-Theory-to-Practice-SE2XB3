from rbt import RBTree

import random
import math
import sys


class BSTNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def __str__(self):
        return "(" + str(self.value) + ")"

    def __repr__(self):
        return "(" + str(self.value) + ")"


class BST:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = BSTNode(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = BSTNode(value)
                node.left.parent = node
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = BSTNode(value)
                node.right.parent = node
            else:
                self.__insert(node.right, value)
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"


# without duplicates
def create_random_list(n):
    L = [i for i in range(1, n+1)]
    random.shuffle(L)
    return L

def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

def timetest_tree_heights_random(n):
    total = 0
    for _ in range(n):
        rand_list = create_random_list(10000)
        bst = BST()
        rbt = RBTree()
        for i in rand_list:
            bst.insert(i)
            rbt.insert(i)
        total += bst.get_height() - rbt.get_height()
    return total / n

# print(timetest_tree_heights_random(100))

def timetest_worstcase():
    factor = 0
    total1 = 0
    total2 = 0
    for _ in range(10000):
        bst = BST()
        rbt = RBTree()
        L = create_near_sorted_list(100, factor)
        for i in L:
            bst.insert(i)
            rbt.insert(i)
        total1 = bst.get_height()
        total2 = rbt.get_height()
        factor += 0.0001
        print(round(factor, 4), total1, total2)

# timetest_worstcase()