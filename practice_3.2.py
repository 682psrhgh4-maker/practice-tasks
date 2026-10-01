#3 task
def hill_climbing(values, start):
    current = start
    while True:
        neighbors = []
        if current > 0:
            neighbors.append(current - 1)
        if current < len(values) - 1:
            neighbors.append(current + 1)
        best = current
        for n in neighbors:
            if values[n] > values[best]:
                best = n
        if best == current:
            break
        current = best
    return current
values2 = [1, 4, 7, 5, 3, 6, 9, 8]
res_start0 = hill_climbing(values2, 0)
res_start4 = hill_climbing(values2, 4)

print(f"start = 0 -> Соңғы индекс: {res_start0}, Мәні: {values2[res_start0]}")
print(f"start = 4 -> Соңғы индекс: {res_start4}, Мәні: {values2[res_start4]}")
