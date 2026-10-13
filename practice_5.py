states = ["A", "B", "C", "D", "E", "S", "F", "H", "I"]
actions = ["UP", "DOWN", "LEFT", "RIGHT"]
gamma, theta = 0.9, 0.001

pos = {
    "A":(0,0), "B":(0,1), "C":(0,2), "G":(0,3),
    "D":(1,0),            "E":(1,2), "X":(1,3),
    "S":(2,0), "F":(2,1), "H":(2,2), "I":(2,3)
}
grid = {p: s for s, p in pos.items()}
moves = {"UP":(-1,0), "DOWN":(1,0), "LEFT":(0,-1), "RIGHT":(0,1)}

outcomes = {
    "UP": [("UP", .8), ("LEFT", .1), ("RIGHT", .1)],
    "DOWN": [("DOWN", .8), ("RIGHT", .1), ("LEFT", .1)],
    "LEFT": [("LEFT", .8), ("DOWN", .1), ("UP", .1)],
    "RIGHT": [("RIGHT", .8), ("UP", .1), ("DOWN", .1)]
}

def move(s, d):
    r, c = pos[s]
    dr, dc = moves[d]
    return grid.get((r + dr, c + dc), s)

def get_q(s, a, V):
    q = 0.0
    for d, prob in outcomes[a]:
        nxt = move(s, d)

        if nxt == "G":
            r = 10.0
        elif nxt == "X":
            r = -10.0
        else:
            r = -0.1

        nxt_v = 0.0 if nxt in ["G", "X"] else V[nxt]
        q += prob * (r + gamma * nxt_v)
    return q

# Value Iteration
V = {s: 0.0 for s in states}
while True:
    new_V = {s: max(get_q(s, a, V) for a in actions) for s in states}
    delta = max(abs(new_V[s] - V[s]) for s in states)
    V = new_V
    if delta < theta:
        break

# Соңғы саясат (Policy)
policy = {s: max(actions, key=lambda a: get_q(s, a, V)) for s in states}

print("КҮЙ МӘНДЕРІ (V):")
for s, v in V.items():
    print(f"{s}: {round(v, 3)}")

print("\nСАЯСАТ (Policy):")
for s, a in policy.items():
    print(f"pi({s}) = {a}")
