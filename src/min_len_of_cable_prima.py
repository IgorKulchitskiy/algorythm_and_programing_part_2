class Node:
    def __init__(self, value, priority):
        self.left = None
        self.right = None
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        if self.root is None:
            self.root = Node(value, priority)
        else:
            self.inner_insert(self.root, value, priority)

    def inner_insert(self, node, value, priority):
        if priority >= node.priority:
            if node.left is None:
                node.left = Node(value, priority)
            else:
                self.inner_insert(node.left, value, priority)
        else:
            if node.right is None:
                node.right = Node(value, priority)
            else:
                self.inner_insert(node.right, value, priority)

    def delete_min(self):
        if self.root is None:
            return None
        else:
            return self.inner_delete_min(self.root)

    def inner_delete_min(self, node):
        if node.left is not None:
            min_node = self.inner_delete_min(node.left)
            if node.left.priority == min_node.priority:
                node.left = None
            return min_node
        else:
            min_node = Node(node.value, node.priority)
            self.root = node.right
            return min_node


def read_input(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            well1, well2, distance = line.strip().split(', ')
            distance = int(distance)
            if well1 not in graph:
                graph[well1] = []
            if well2 not in graph:
                graph[well2] = []
            graph[well1].append((well2, distance))
            graph[well2].append((well1, distance))
    return graph


def prim(graph):
    visited = set()
    min_prim_tree = []
    pq = PriorityQueue()
    start_node = next(iter(graph))
    visited.add(start_node)
    for neighbor, cost in graph[start_node]:
        pq.insert((start_node, neighbor, cost), cost)

    while pq.root:
        edge = pq.delete_min()
        cost, current, next_node = edge.priority, edge.value[0], edge.value[1]
        if next_node not in visited:
            visited.add(next_node)
            min_prim_tree.append((current, next_node, cost))
            for neighbor, n_cost in graph[next_node]:
                if neighbor not in visited:
                    pq.insert((next_node, neighbor, n_cost), n_cost)

    if len(visited) != len(graph):
        return -1
    else:
        return sum(cost for _, _, cost in min_prim_tree)


file_path = "communication_wells.csv"
graph = read_input(file_path)
min_cable_length = prim(graph)
print("Min Cable Length:", min_cable_length)
