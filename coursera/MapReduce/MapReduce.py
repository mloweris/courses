class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for key in data:
            mapper(self, key, data[key])

        for key in self.intermediate:
            reducer(self, key, self.intermediate[key])

        for item in self.result:
            print item

def execute(data, mapper, reducer):
    mr = MapReduce()
    mr.execute(data, mapper, reducer)
