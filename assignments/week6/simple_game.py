# Week 6 Assignment
# Simple Inventory Game

# ---------------- INVENTORY ----------------
inventory = []

# ---------------- ROOM ITEMS ----------------
items_in_room = [
    {"name": "apple"},
    {"name": "key"},
    {"name": "torch"}
]

# Inventory limit
MAX_ITEMS = 5


# ---------------- FUNCTIONS ----------------
def show_room_items():
    print("\nItems in room:")

    for item in items_in_room:
        print("-", item["name"])


def show_inventory():
    print("\nInventory:")

    if len(inventory) == 0:
        print("Inventory is empty.")

    else:
        for item in inventory:
            print("-", item["name"])


def pick_up(item_name):

    if len(inventory) >= MAX_ITEMS:
        print("Inventory full!")
        return

    for item in items_in_room:

        if item["name"] == item_name:
            inventory.append(item)
            items_in_room.remove(item)

            print(item_name, "picked up!")
            return

    print("Item not found.")


def drop(item_name):

    for item in inventory:

        if item["name"] == item_name:
            inventory.remove(item)
            items_in_room.append(item)

            print(item_name, "dropped!")
            return

    print("Item not in inventory.")


def examine(item_name):

    for item in inventory + items_in_room:

        if item["name"] == item_name:
            print("You see a", item_name)
            return

    print("Item not found.")


# ---------------- MAIN FUNCTION ----------------
def main():

    print("Welcome to the Simple Game!")
    print("Type help for commands.")

    while True:

        command = input("\nEnter command: ").lower()

        if command == "room":
            show_room_items()

        elif command == "inventory":
            show_inventory()

        elif command.startswith("pickup "):
            item_name = command.replace("pickup ", "")
            pick_up(item_name)

        elif command.startswith("drop "):
            item_name = command.replace("drop ", "")
            drop(item_name)

        elif command.startswith("examine "):
            item_name = command.replace("examine ", "")
            examine(item_name)

        elif command == "help":
            print("\nCommands:")
            print("room")
            print("inventory")
            print("pickup apple")
            print("drop apple")
            print("examine apple")
            print("quit")

        elif command == "quit":
            print("Game ended.")
            break

        else:
            print("Invalid command.")


# Run program
if __name__ == "__main__":
    main()
