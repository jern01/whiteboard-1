"""
Takes a directed graph and two nodes and checks if there is a path from the first
node to the second node. The search is BFS where nodes are visited in order of
distance from the start. Time complexity is O(V + E) where V is the number of vertices
and E is the number of edges. Space complexity is O(V) for the queue and the parents dictionary.
"""

from collections import deque


def find_path(graph, start, end):
    if start not in graph or end not in graph:
        return False, []

    parents = {start: None}
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = parents[node]
            path.reverse()
            return True, path

        for neighbour in graph[node]:
            if neighbour not in parents:
                parents[neighbour] = node
                queue.append(neighbour)

    return False, []


if __name__ == "__main__":
    graph = {
        "A": ["B"],
        "B": ["A", "C", "D", "E"],
        "C": ["F"],
        "D": ["G", "E"],
        "E": ["F"],
        "F": ["B", "G"],
        "G": [],
    }

    print(find_path(graph, "D", "B"))
    print(find_path(graph, "F", "A"))
    print(find_path(graph, "G", "C"))
