p_high = 10 / 11
p_low = 1 - p_high

actions = {
    'Extra': ([p_high, p_low], [0, -60]),
    'Usual': ([p_high, p_low], [-30, 0])
}

def EU(probs, utilities):
    return sum(p * u for p, u in zip(probs, utilities))

scores = {name: EU(*values)
          for name, values in actions.items()}

print(scores)
print(max(scores, key=scores.get))

import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X_train = np.array([
    [1, 1], [1, 1], [1, 1],
    [1, 0], [1, 0], [0, 1],
    [1, 1], [1, 0], [0, 0],
    [0, 0], [0, 0], [0, 0]
])

y_train = np.array([1, 1, 1, 1, 1, 1,
                    0, 0, 0, 0, 0, 0])

X_test = np.array([[1, 1], [1, 0]])

model = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

model.fit(X_train, y_train)

p = model.predict_proba(X_test)[:, 1]
alerts = (p >= 0.50).astype(int)

print(p)
print(alerts)
