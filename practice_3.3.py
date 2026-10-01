import math
import random


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

def random_restart(values, attempts):
    best_position = None
    for _ in range(attempts):
        start = random.randint(0, len(values) - 1)
        position = hill_climbing(values, start)
        if best_position is None or values[position] > values[best_position]:
            best_position = position
    return best_position
values2 = [1, 4, 7, 5, 3, 6, 9, 8]
for i in range(1, 4):
    res_rr = random_restart(values2, attempts=5)
    print(f"Жіберу {i} Үздік мән = {values2[res_rr]}")
