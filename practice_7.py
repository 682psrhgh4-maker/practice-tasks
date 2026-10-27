states = ["A", "B", "C"]
T = [
    [0.7, 0.3, 0.0],
    [0.2, 0.6, 0.2],
    [0.0, 0.3, 0.7]
]
emission = {
    "RED": [0.8, 0.5, 0.2],
    "BLUE": [0.2, 0.5, 0.8]
}
belief = [0.5, 0.3, 0.2]
readings = ["RED", "BLUE", "BLUE", "RED"]
def predict(b, T):
    return [
        sum(b[i] * T[i][j] for i in range(3))
        for j in range(3)
    ]
def update(pred, likelihood):
    weights = [
        pred[i] * likelihood[i]
        for i in range(3)
    ]

    total = sum(weights)

    return [w / total for w in weights]

for step, reading in enumerate(readings, 1):
    prediction = predict(belief, T)
    belief = update(prediction, emission[reading])

    print(f"{step}-қадам: {reading}")

    for i in range(3):
        print(f"{states[i]}: {belief[i]:.4f}")

    best = states[belief.index(max(belief))]
    print("Ең ықтимал аймақ:", best)
    print()
