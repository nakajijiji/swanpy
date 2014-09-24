class SimpleSearch:
    def __init__(self):
        self.indexMap = {}

    def add(self, item):
        for f in item.features:
            if f in self.indexMap:
                self.indexMap[f].append(item.obj)
            else:
                self.indexMap[f] = [item.obj]
    
    def search(self, features):
        objs = []
        for f in features:
            if not (f in self.indexMap):
                return []
            objs.append(self.indexMap[f])
        
        result = set(objs.pop(0))
        for o in objs:
            s = set(o)
            result = result & s
        return result

class Item:
    def __init__(self, features, obj):
        self.features = features
        self.obj = obj
