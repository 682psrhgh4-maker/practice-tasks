def random_neighbor(current, n):
    neighbors = []
    if current > 0:
        neighbors.append(current - 1)
    if current < n - 1:
        neighbors.append(current + 1)
    return random.choice(neighbors)

def anneal(values, start, T=10):
    current = start
    while T > 0.1:
        next_state = random_neighbor(current, len(values))
        dE = values[next_state] - values[current]
        if dE > 0 or random.random() < math.exp(dE / T):
            current = next_state
        T *= 0.95
    return current



# 5 task
print("5 task")
for i in range(1, 6):
    res_sa = anneal(values2, start=0, T=10)
    print(f"Жіберу{i}: Нәтиже = {values2[res_sa]}")
