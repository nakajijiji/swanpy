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
    
    def __create_parent(self, first, second):
        parent = Node(None, first.value + second.value)
        parent.set_children([first, second])
        first.set_parent(parent)
        second.set_parent(parent)
        return parent

    def toCodeMap(self):
        if self.top == None:
            return None
        current = self.top
        result = {}
        codes = [0]
        self.__search(result, codes, current)
        return result
                
    def __search(self, result, codes, node):
        if node.item != None:
            result[Huffman.toKey(codes)] = node.item
            return

        index = 0
        for c in node.children:
            codesCopy = list(codes) 
            codesCopy.append(index)
            self.__search(result, codesCopy, c)
            index+=1
    
    @staticmethod
    def toKey(codes):
        result = ""
        for c in codes:
            result += str(c)
        return result

class Node:
    def __init__(self, item, value):
        self.item = item
        self.value = value

    def set_parent(self, parent):
        self.parent = parent

    def set_children(self, children):
        self.children = children
