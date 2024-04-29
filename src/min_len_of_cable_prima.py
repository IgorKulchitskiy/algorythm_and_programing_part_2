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
    start_node = next(iter(graph))
    visited.add(start_node)
    edges = [(cost, start_node, neighbor) for neighbor, cost in graph[start_node]]
    edges.sort()

    while edges:
        cost, current, next_node = edges.pop(0)
        if next_node not in visited:
            visited.add(next_node)
            min_prim_tree.append((current, next_node, cost))
            for neighbor, n_cost in graph[next_node]:
                if neighbor not in visited:
                    edges.append((n_cost, next_node, neighbor))
            edges.sort()

    if len(visited) != len(graph):
        return -1
    else:
        return sum(cost for _, _, cost in min_prim_tree)


file_path = "communication_wells.csv"
graph = read_input(file_path)
min_cable_length = prim(graph)
print("Min Cable Length:", min_cable_length)
