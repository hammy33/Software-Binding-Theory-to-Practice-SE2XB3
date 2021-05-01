class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def get_grandparent(self):
        return self.parent.parent

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        x = self.parent
        if self.left != None:
            if self.parent != None:
                if self.is_left_child():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
            y = self.left.right
            self.parent = self.left
            self.parent.right = self
            self.parent.parent = x
            self.left = y
            if self.left != None:
                self.left.parent = self

    def rotate_left(self):
        x = self.parent
        if self.right != None:
            if self.parent != None:
                if self.is_left_child():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
            y = self.right.left
            self.parent = self.right
            self.parent.left = self
            self.parent.parent = x
            self.right = y
            if self.right != None:
                self.right.parent = self



class RBTree:

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
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        while node != None and node.parent != None and node.parent.is_red(): # violation
            if node.uncle_is_black():
                if node.parent.is_left_child():
                    if node.is_left_child(): # line (case 3)
                        node.get_grandparent().rotate_right()
                        # recolour
                        node.parent.make_black()
                        node.get_brother().make_red()
                    else: # triangle (case 2)
                        node.parent.rotate_left()
                        # recheck (guaranteed)
                        node = node.left
                else:
                    if node.is_right_child():
                        node.get_grandparent().rotate_left()
                        node.parent.make_black()
                        node.get_brother().make_red()
                    else:
                        node.parent.rotate_right()
                        node = node.right
            else: # (case 1)
                # recolour
                node.get_uncle().make_black()
                node.parent.make_black()
                node.get_grandparent().make_red()
                # recheck
                node = node.get_grandparent()
        # update root
        while self.root.parent != None:
            self.root = self.root.parent
        self.root.make_black() # (case 0)

        
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
