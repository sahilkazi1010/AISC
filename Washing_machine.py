#washing Machine 


# Washing Machine Fuzzy Logic Controller
# Inputs: Dirt Level and Grease Level
# Output: Wash Time

def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif x == b:
        return 1
    elif x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)


# USER INPUT
dirt = float(input("Enter Dirt Level (0-100): "))
grease = float(input("Enter Grease Level (0-100): "))

# FUZZIFICATION
dirt_low = triangular(dirt, 0, 25, 50)
dirt_medium = triangular(dirt, 25, 50, 75)
dirt_high = triangular(dirt, 50, 75, 100)

grease_low = triangular(grease, 0, 25, 50)
grease_medium = triangular(grease, 25, 50, 75)
grease_high = triangular(grease, 50, 75, 100)

print("\n--- Membership Values ---")
print("Dirt")
print("Low =", round(dirt_low, 2))
print("Medium =", round(dirt_medium, 2))
print("High =", round(dirt_high, 2))

print("\nGrease")
print("Low =", round(grease_low, 2))
print("Medium =", round(grease_medium, 2))
print("High =", round(grease_high, 2))

# RULE EVALUATION (MIN)
R1 = min(dirt_low, grease_low)       # Very Short
R2 = min(dirt_low, grease_medium)    # Short
R3 = min(dirt_low, grease_high)      # Medium
R4 = min(dirt_medium, grease_low)    # Short
R5 = min(dirt_medium, grease_medium) # Medium
R6 = min(dirt_medium, grease_high)   # Long
R7 = min(dirt_high, grease_low)      # Medium
R8 = min(dirt_high, grease_medium)   # Long
R9 = min(dirt_high, grease_high)     # Very Long

# AGGREGATION (MAX)
very_short = R1
short = max(R2, R4)
medium = max(R3, R5, R7)
long_time = max(R6, R8)
very_long = R9

# DEFUZZIFICATION (WEIGHTED AVERAGE)
VS = 10
S = 20
M = 30
L = 40
VL = 50

numerator = (
    very_short * VS +
    short * S +
    medium * M +
    long_time * L +
    very_long * VL
)

denominator = (
    very_short +
    short +
    medium +
    long_time +
    very_long
)

if denominator == 0:
    wash_time = 0
else:
    wash_time = numerator / denominator

# OUTPUT
print("\n--- Rule Strengths ---")
print("Very Short =", round(very_short, 2))
print("Short =", round(short, 2))
print("Medium =", round(medium, 2))
print("Long =", round(long_time, 2))
print("Very Long =", round(very_long, 2))

print("\nEstimated Wash Time =", round(wash_time, 2), "minutes")

if wash_time < 15:
    print("Recommendation: Very Short Wash")
elif wash_time < 25:
    print("Recommendation: Short Wash")
elif wash_time < 35:
    print("Recommendation: Medium Wash")
elif wash_time < 45:
    print("Recommendation: Long Wash")
else:
    print("Recommendation: Very Long Wash")
