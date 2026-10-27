#Washing Machine

pip install scikit-fuzzy matplotlib numpy


# Washing Machine Fuzzy Logic Controller
# Using scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# INPUT VARIABLES
dirt = ctrl.Antecedent(np.arange(0, 101, 1), 'dirt')
grease = ctrl.Antecedent(np.arange(0, 101, 1), 'grease')

# OUTPUT VARIABLE
wash_time = ctrl.Consequent(
    np.arange(0, 61, 1), 'wash_time'
)

# MEMBERSHIP FUNCTIONS: DIRT
dirt['low'] = fuzz.trimf(dirt.universe, [0, 25, 50])
dirt['medium'] = fuzz.trimf(dirt.universe, [25, 50, 75])
dirt['high'] = fuzz.trimf(dirt.universe, [50, 75, 100])

# MEMBERSHIP FUNCTIONS: GREASE
grease['low'] = fuzz.trimf(grease.universe, [0, 25, 50])
grease['medium'] = fuzz.trimf(grease.universe, [25, 50, 75])
grease['high'] = fuzz.trimf(grease.universe, [50, 75, 100])

# MEMBERSHIP FUNCTIONS: WASH TIME
wash_time['very_short'] = fuzz.trimf(
    wash_time.universe, [0, 10, 20]
)
wash_time['short'] = fuzz.trimf(
    wash_time.universe, [10, 20, 30]
)
wash_time['medium'] = fuzz.trimf(
    wash_time.universe, [20, 30, 40]
)
wash_time['long'] = fuzz.trimf(
    wash_time.universe, [30, 40, 50]
)
wash_time['very_long'] = fuzz.trimf(
    wash_time.universe, [40, 50, 60]
)

# RULES
rule1 = ctrl.Rule(
    dirt['low'] & grease['low'], wash_time['very_short']
)
rule2 = ctrl.Rule(
    dirt['low'] & grease['medium'], wash_time['short']
)
rule3 = ctrl.Rule(
    dirt['low'] & grease['high'], wash_time['medium']
)
rule4 = ctrl.Rule(
    dirt['medium'] & grease['low'], wash_time['short']
)
rule5 = ctrl.Rule(
    dirt['medium'] & grease['medium'], wash_time['medium']
)
rule6 = ctrl.Rule(
    dirt['medium'] & grease['high'], wash_time['long']
)
rule7 = ctrl.Rule(
    dirt['high'] & grease['low'], wash_time['medium']
)
rule8 = ctrl.Rule(
    dirt['high'] & grease['medium'], wash_time['long']
)
rule9 = ctrl.Rule(
    dirt['high'] & grease['high'], wash_time['very_long']
)

# CONTROL SYSTEM
washing_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5,
    rule6, rule7, rule8, rule9
])

washing = ctrl.ControlSystemSimulation(washing_ctrl)

# USER INPUT
d = float(input("Enter Dirt Level (0-100): "))
g = float(input("Enter Grease Level (0-100): "))

washing.input['dirt'] = d
washing.input['grease'] = g

# COMPUTE
washing.compute()

# OUTPUT
print(
    "\nEstimated Wash Time =",
    round(washing.output['wash_time'], 2),
    "minutes"
)

# DISPLAY GRAPHS
dirt.view()
grease.view()
wash_time.view(sim=washing)
