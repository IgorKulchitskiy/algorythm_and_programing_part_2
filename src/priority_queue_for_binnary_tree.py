#4__

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

class PriorityQueue:
    def __init__(self):
        self.root = None

    def add_task(self, value, priority):
        if not self.root:
            self.root = Node(value, priority)
            return

        def _add_task_to_node(node):
            if priority <= node.priority:
                if node.left is None:
                    node.left = Node(value, priority)
                else:
                    _add_task_to_node(node.left)
            else:
                if node.right is None:
                    node.right = Node(value, priority)
                else:
                    _add_task_to_node(node.right)

        _add_task_to_node(self.root)

    def remove_highest_priority_task(self):
        if not self.root:
            return None

        def _find_highest_priority_task(node):
            if node.right is None:
                return node.value, node.priority
            return _find_highest_priority_task(node.right)

        def _remove_task(node, value):
            if node is None:
                return None

            if node.value == value:
                return None 

            if node.left and node.left.value == value:
                node.left = None
            elif node.right and node.right.value == value:
                node.right = None
            else:
                _remove_task(node.left, value)
                _remove_task(node.right, value)

        value, priority = _find_highest_priority_task(self.root)
        _remove_task(self.root, value)
        return value, priority

    def traverse(self):
        def _traverse(node):
            if node is None:
                return []

            return _traverse(node.left) + [(node.value, node.priority)] + _traverse(node.right)

        return _traverse(self.root)


if __name__ == "__main__":
    priority_queue = PriorityQueue()
    priority_queue.add_task("Task 1", 3)
    priority_queue.add_task("Task 2", 1)
    priority_queue.add_task("Task 3", 2)
    
    print("Ініціалізація черги:")
    print(priority_queue.traverse())
    
    print("\nВидалення елемента з найвищим пріорітетом:")
    print(priority_queue.remove_highest_priority_task())
    
    print("\nЧерга після видалення:")
    print(priority_queue.traverse())
