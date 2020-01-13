
"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


class Graph(object):

    def __init__(self, graph: dict):
        self._collection = []
        _visited = set()

        for vertex in graph.keys():
            _temp = [vertex]
            for item in _temp:
                if item in _visited:
                    continue
                _visited.add(item)
                _temp.extend(graph.get(item, []))
                self._collection.append(item)

    def __iter__(self):
        return iter(self._collection)

    def __getitem__(self, key):
        return self._collection[key]

    def __len__(self):
        return len(self._collection)


if __name__ == "__main__":

    E1 = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
    E2 = {'B': ['C'], 'A': ['B', 'C', 'D'], 'C': [], 'D': ['A']}

    graph1 = Graph(E1)
    print("graph1:")

    for i in graph1:
        print(i)

    graph2 = Graph(E2)
    print("graph2:")

    for i in graph2:
        print(i)

    print("zip:")

    for i, j in zip(graph1, graph2):
        print(i, j)
