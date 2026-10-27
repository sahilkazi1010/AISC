#neuro-Fuzzy

pip install numpy scikit-fuzzy scikit-learn


import numpy as np
import skfuzzy as fuzz
from sklearn.linear_model import LinearRegression

# STEP 1: TRAINING DATA
X = np.array([
    [2, 3],
    [3, 4],
    [5, 5],
    [6, 7],
    [8, 8],
    [9, 10]
])

y = np.array([18, 22, 40, 50, 60, 70])

# STEP 2: UNIVERSE OF DISCOURSE
u = np.arange(0, 11, 1)

# STEP 3: CREATE FUZZY FEATURES
features = []

for dirt, load in X:
    # Dirtiness Memberships
    d_low = fuzz.interp_membership(
        u, fuzz.trimf(u, [0, 0, 5]), dirt
    )
    d_med = fuzz.interp_membership(
        u, fuzz.trimf(u, [0, 5, 10]), dirt
    )
    d_high = fuzz.interp_membership(
        u, fuzz.trimf(u, [5, 10, 10]), dirt
    )

    # Load Memberships
    l_small = fuzz.interp_membership(
        u, fuzz.trimf(u, [0, 0, 5]), load
    )
    l_med = fuzz.interp_membership(
        u, fuzz.trimf(u, [0, 5, 10]), load
    )
    l_large = fuzz.interp_membership(
        u, fuzz.trimf(u, [5, 10, 10]), load
    )

    # Rule Strengths
    r1 = min(d_low, l_small)
    r2 = min(d_med, l_med)
    r3 = min(d_high, l_large)

    features.append([r1, r2, r3])

features = np.array(features)

# STEP 4: TRAIN LINEAR REGRESSION MODEL
model = LinearRegression()
model.fit(features, y)

print("=====================================")
print("MODEL TRAINED SUCCESSFULLY")
print("=====================================")

print("\nLearned Rule Weights:")
print("Rule 1 Weight =", round(model.coef_[0], 2))
print("Rule 2 Weight =", round(model.coef_[1], 2))
print("Rule 3 Weight =", round(model.coef_[2], 2))
print("Bias =", round(model.intercept_, 2))

# STEP 5: USER INPUT
print("\n=====================================")
print("TESTING PHASE")
print("=====================================")

dirt = float(input("Enter Dirtiness (0-10): "))
load = float(input("Enter Load Size (0-10): "))

# STEP 6: FUZZIFICATION
d_low = fuzz.interp_membership(
    u, fuzz.trimf(u, [0, 0, 5]), dirt
)
d_med = fuzz.interp_membership(
    u, fuzz.trimf(u, [0, 5, 10]), dirt
)
d_high = fuzz.interp_membership(
    u, fuzz.trimf(u, [5, 10, 10]), dirt
)

l_small = fuzz.interp_membership(
    u, fuzz.trimf(u, [0, 0, 5]), load
)
l_med = fuzz.interp_membership(
    u, fuzz.trimf(u, [0, 5, 10]), load
)
l_large = fuzz.interp_membership(
    u, fuzz.trimf(u, [5, 10, 10]), load
)

# STEP 7: DISPLAY MEMBERSHIP VALUES
print("\n=====================================")
print("MEMBERSHIP VALUES")
print("=====================================")

print("\nDirtiness")
print("Low =", round(d_low, 3))
print("Medium =", round(d_med, 3))
print("High =", round(d_high, 3))

print("\nLoad Size")
print("Small =", round(l_small, 3))
print("Medium =", round(l_med, 3))
print("Large =", round(l_large, 3))

# STEP 8: RULE EVALUATION
r1 = min(d_low, l_small)
r2 = min(d_med, l_med)
r3 = min(d_high, l_large)

print("\n=====================================")
print("RULE STRENGTHS")
print("=====================================")

print("Rule 1 (Low AND Small) =", round(r1, 3))
print("Rule 2 (Medium AND Medium) =", round(r2, 3))
print("Rule 3 (High AND Large) =", round(r3, 3))

# STEP 9: PREDICTION
test = np.array([[r1, r2, r3]])
predicted_time = model.predict(test)

# STEP 10: FINAL OUTPUT
print("\n=====================================")
print("FINAL RESULT")
print("=====================================")

print(
    "Predicted Wash Time =",
    round(predicted_time[0], 2),
    "minutes"
)
