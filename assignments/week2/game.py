import time

# typing effect
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)
    print()

slow_print("🚀 Initializing Space Mission Simulation...")
time.sleep(1)

name = input("Enter astronaut name: ")
slow_print(f"Welcome, Commander {name}.")
time.sleep(1)

slow_print("Your ship is approaching an unknown planet...")
choice1 = input("Do you 'land' or 'scan' the planet? ").lower()

# Branch 1
if choice1 == "scan":
    slow_print("🔍 Scanning planet surface...")
    time.sleep(1)
    
    signal = input("A strange signal appears. Do you 'follow' or 'ignore'? ").lower()
    
    # Nested condition
    if signal == "follow":
        slow_print("You discover alien technology! 👽")
    else:
        slow_print("You miss a major discovery and move on.")

# Branch 2
elif choice1 == "land":
    slow_print("🪐 Landing sequence initiated...")
    time.sleep(1)

    # number input with validation
    while True:
        try:
            fuel = int(input("Set landing power (1-10): "))
            if 1 <= fuel <= 10:
                break
            else:
                print("❌ Choose a number between 1 and 10.")
        except:
            print("❌ Invalid input. Enter a number.")

    if fuel < 4:
        slow_print("⚠️ Too weak! You crash on landing.")
    elif 4 <= fuel <= 7:
        slow_print("✅ Safe landing. You explore the planet.")
        
        explore = input("Do you enter a cave? (yes/no) ").lower()
        
        if explore == "yes":
            slow_print("You find glowing crystals 💎")
        else:
            slow_print("You stay safe but discover nothing.")
    else:
        slow_print("🚀 Too much power! You overshoot and return to space.")

# Invalid input branch
else:
    slow_print("Command not recognized. Mission aborted.")

slow_print("🛰️ Simulation complete. Goodbye Commander.")
