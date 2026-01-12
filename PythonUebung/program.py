from helpers.reflection_helper import ModuleReflector

reflector = ModuleReflector("aufgaben")
aufgaben = reflector.get_functions()
is_running = True

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
        if(user_input == "q" or user_input == "Q"):
            is_running = False
        else:
            print(f"\nEs wurde eine Zahl erwartet.")

print("Programm wurde beendet.")
