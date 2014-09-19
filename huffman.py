class Huffman:
    def build(self, countMap):
        queue = []
        for k, v in sorted(countMap.items(), key=lambda x:x[1]):
            node = Node(k, v)
            queue.append(node)
            if len(queue) == 3:
                sorted(queue)
                first = queue.pop(0)
                second = queue.pop(0)
                parent = self.__create_parent(first, second)
                queue.append(parent)
        if len(queue) == 1:
            self.top = queue.pop(0)
        elif len(queue) == 2:
            first = queue.pop(0)
            second = queue.pop(0)
            parent = self.__create_parent(first, second)
            self.top = parent

    def value(self):
        print self.top.value
    
    def __create_parent(self, first, second):
        parent = Node(None, first.value + second.value)
        parent.set_children(first, second)
        first.set_parent(parent)
        second.set_parent(parent)
        return parent

class Node:
    def __init__(self, item, value):
        self.item = item
        self.value = value

    def set_parent(self, parent):
        self.parent = parent

    def set_children(self, first, second):
        self.first = first
        self.second = second

