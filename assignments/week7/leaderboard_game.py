import csv
from datetime import datetime
import os

# Debug flag
DEBUG = True

# File name
FILE_NAME = "records.csv"

# ----------------------------
# Get player name
# ----------------------------
name = input("Enter your name: ")

# ----------------------------
# DEBUG MODE
# ----------------------------
if DEBUG:
    print("DEBUG MODE ACTIVE")
    score = 50   # Placeholder score for testing

# ----------------------------
# NORMAL GAME MODE
# ----------------------------
else:
    print("Welcome to the game!")

    # Simple example game
    answer = 7
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == answer:
        score = 100
        print("Correct!")
    else:
        score = 0
        print("Wrong answer!")

# ----------------------------
# Create timestamp
# ----------------------------
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ----------------------------
# Save record
# ----------------------------
try:
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        # Write header if file does not exist
        if not file_exists:
            writer.writerow(["Name", "Timestamp", "Score"])

        # Add current result
        writer.writerow([name, timestamp, score])

    print("Record saved successfully!")

except Exception as e:
    print("Error saving file:", e)

# ----------------------------
# Load and display leaderboard
# ----------------------------
print("\n--- LEADERBOARD ---")

records = []

try:
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        for row in reader:
            records.append(row)

    # Sort by score (highest first)
    records.sort(key=lambda x: int(x[2]), reverse=True)

    # Display leaderboard
    for record in records:
        print(f"Name: {record[0]} | Time: {record[1]} | Score: {record[2]}")

except Exception as e:
    print("Error loading leaderboard:", e)
