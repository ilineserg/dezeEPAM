
"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


class Graph:

    visited = {}

    def __init__(self, E):
        self.E = E
        self.visited = set()
        self.childs = list(self.E.keys())[:1]

    def __iter__(self):
        for child in self.childs:
            if child not in self.visited:
                self.visited.add(child)
                self.childs.extend(self.E.get(child, []))
                yield child


E = {'A': ['X', 'Y', 'Z'], 'B': ['C', 'D'], 'X': ['H', 'J'], 'Y': ['K', 'I']}
graph = Graph(E)

for vertex in graph:
    print(vertex)