class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
    

def earliest_ancestor(ancestors, starting_node):
    def get_parents(child):
        return [pair[0] for pair in ancestors if pair[1] == child]
    
    visited = set()
    s = Stack()
    s.push([starting_node])
    longest_ancestor_path = []
    while s.size() > 0:
        path = s.pop()
        last_child = path[-1]
        parents = get_parents(last_child)
        if not len(parents):
            if len(path) > len(longest_ancestor_path) or (len(path) == len(longest_ancestor_path) and path[-1] < longest_ancestor_path[-1]):
                longest_ancestor_path = path
        visited.add(last_child)
        for parent in parents:
            copy = path.copy()
            copy.append(parent)
            s.push(copy)
    return longest_ancestor_path[-1]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 7))