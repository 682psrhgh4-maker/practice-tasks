import heapq

# Граф: {түйін: [(көрші, шығын_g)]}
graph = {
    'S': [('A', 2), ('B', 4)],
    'A': [('C', 3)],
    'B': [('D', 3)],
    'C': [('G', 2)],
    'D': [('G', 1)],
    'G': []
}

# Эвристика h(n)
heuristic = {
    'S': 7, 'A': 6, 'B': 2,
    'C': 4, 'D': 1, 'G': 0
}

def a_star_search(start, goal):
    # Priority Queue: (f_score, g_score, current_node, path)
    pq = [(heuristic[start], 0, start, [start])]
    visited = {}

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current == goal:
            return path, g

        if current not in visited or g < visited[current]:
            visited[current] = g
            for neighbor, weight in graph.get(current, []):
                new_g = g + weight
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

# Іске қосу
start_node = 'S'
goal_node = 'G'
path, total_cost = a_star_search(start_node, goal_node)

print(f"Табылған жол: {' -> '.join(path)}")
print(f"Жалпы шығын: {total_cost}")
