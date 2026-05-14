import random


# ---------------------------------------------------------
# STEP 1 : TAKE INPUTS
# ---------------------------------------------------------

x = float(input("Enter Input Value        : "))
weight = float(input("Enter Initial Weight    : "))
bias = float(input("Enter Bias              : "))
target = float(input("Enter Target Output     : "))
learning_rate = float(input("Enter Learning Rate     : "))

print("\nINPUT VALUE       :", x)
print("INITIAL WEIGHT    :", weight)
print("BIAS              :", bias)
print("TARGET OUTPUT     :", target)
print("LEARNING RATE     :", learning_rate)

# ---------------------------------------------------------
# STEP 2 : TRAINING LOOP
# ---------------------------------------------------------

print("\n===================================================")
print("TRAINING STARTED")
print("===================================================\n")

for step in range(1, 6):   # 5 steps enough for demo

    print(f"\n------------ STEP {step} ------------")

    # -------------------------------------------------
    # STEP 3 : PREDICTION (Forward Pass)
    # -------------------------------------------------
    predicted_output = (x * weight) + bias

    print("\nPREDICTION")
    print(f"Predicted Output = ({x} * {weight}) + {bias} = {predicted_output}")

    # -------------------------------------------------
    # STEP 4 : ERROR CALCULATION
    # -------------------------------------------------
    error = target - predicted_output

    print("\nERROR")
    print(f"Error = {target} - {predicted_output} = {error}")

    # -------------------------------------------------
    # STEP 5 : WEIGHT UPDATE (Gradient Descent)
    # -------------------------------------------------
    print("\nWEIGHT UPDATE")

    old_weight = weight
    print(f"Old Weight = {old_weight}")

    # Gradient Descent Rule
    weight = weight + (learning_rate * error * x)

    print(f"Updated Weight = {weight}")

# ---------------------------------------------------------
# FINAL RESULT
# ---------------------------------------------------------

print("\n===================================================")
print("FINAL RESULT")
print("===================================================\n")

final_output = (x * weight) + bias

print("Final Weight     :", weight)
print("Final Prediction :", final_output)
print("Target Output    :", target)