from helpers.reflection_helper import ModuleReflector
from my_io.command import Command

commands = Command.create_all()
is_running = True
aufgaben = ModuleReflector("aufgaben").get_functions()

while (is_running):
    print("Wählen Sie eine Aufgabe aus.")
    user_input = input()

    try:
        num = int(user_input) - 1
        if (num > -1 and num < len(aufgaben)):
            aufgaben[num]()
        else:
            print(f"Wähle eine Aufgabe zwischen 1 und {len(aufgaben)}.")
        print()

    except ValueError:
        split = user_input.split()
        if(len(split)is 0):
            print("\nEs gab kein Input.")
            continue

        for c in commands:
            if(c.name == split[0].lower()):
                out = c.execute(split[1:])
                if(out is not None):
                    aufgaben = ModuleReflector(str(out)).get_functions()
                break
        else:
            print(f"\nEs wurde eine Zahl erwartet.")
