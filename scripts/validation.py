# scripts/validation.py
print("Validation Step: Checking data...")
try:
    with open("etl_output.txt", "r") as f:
        lines = f.readlines()
        if lines:
            print("Validation passed. Data exists.")
        else:
            print("Validation failed. File is empty.")
except FileNotFoundError:
    print("Validation failed. etl_output.txt not found.")
