
"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


class Graph(object):
    _collection = []

    def __init__(self, graph: dict):
        _visited = set()
        _temp = list(graph.keys())[:1]

        for item in _temp:
            if item not in _visited:
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

    E = {'A': ['B', 'D', 'X'], 'B': ['Y', 'C'], 'C': ['Z'], 'D': ['A']}
    graph = Graph(E)

    for vertex in graph:
        print(vertex)

    print("*" * 3)

    for vertex in graph:
        print(vertex)

    print("*" * 3)
    print("Len:", len(graph))
    print("graph[3]:", graph[3])