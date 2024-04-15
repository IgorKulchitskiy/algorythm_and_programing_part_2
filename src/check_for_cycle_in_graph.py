#5
def has_cycle(graph):
    visited = set()
    parent = {}
    
    def dfs(node, parent_node):
        visited.add(node)
        parent[node] = parent_node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent_node:
                return True
                
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
                
    return False

def check_for_cycle_in_graph(graph, output_file):
    has_cycle_result = has_cycle(graph)
    
    with open(output_file, 'w') as file:
        if has_cycle_result:
            file.write("Граф містить цикл.")
        else:
            file.write("Граф не містить цикл.")

    return has_cycle_result

if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [1, 3, 5],
        3: [1, 2, 4],
        4: [3, 5],
        5: [2, 4]
    }
    result = check_for_cycle_in_graph(graph, "output.txt")
