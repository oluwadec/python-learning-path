"""07_text_adventure.py - Mini project: rooms, exits, and a tiny story."""

ROOMS = {
    "hall": {"text": "A dusty hall with two doors.", "exits": {"north": "library", "east": "kitchen"}},
    "library": {"text": "Shelves of old books. A key lies on a table.", "exits": {"south": "hall"}, "item": "key"},
    "kitchen": {"text": "A locked door leads outside.", "exits": {"west": "hall"}, "locked_exit": "garden"},
    "garden": {"text": "Fresh air! You escaped.", "exits": {}},
}


def run(commands: list) -> None:
    room = "hall"
    inventory = []

    for command in commands:
        print(f"> {command}")
        if command.startswith("go "):
            direction = command[3:]
            exits = ROOMS[room]["exits"]
            if direction in exits:
                room = exits[direction]
            else:
                print("You can't go that way.")
                continue
        elif command == "take" and "item" in ROOMS[room]:
            inventory.append(ROOMS[room]["item"])
            print("You picked up:", inventory[-1])
            continue
        elif command == "unlock" and room == "kitchen":
            if "key" in inventory:
                ROOMS["kitchen"]["exits"]["outside"] = "garden"
                print("The door unlocks.")
            else:
                print("You need a key.")
            continue
        print(ROOMS[room]["text"])


if __name__ == "__main__":
    run(["go north", "take", "go south", "go east", "go outside", "unlock", "go outside"])
