from helpers.io_helper import request_input

def aufgabe1():
    print("Hello, World!")

def aufgabe2():
    print("Wie ist dein Vorname?")
    vorname = input()
    print(f"Hallo, {vorname}")

def aufgabe3():
    num = 3.1415
    print(f"{num}: {type(num)}")

def aufgabe4():
    text = 10
    textAsInt = int(text)
    textAsFloat = float(text)
    print(f"{textAsInt=}")
    print(f"{textAsFloat=}")

def aufgabe5():
    num = 3.1415
    print(round(num, 2))

def aufgabe6():
    user_input = request_input()
    print(f"{user_input}: {type(user_input)}")

def aufgabe7():
    user_input = request_input()
    print(f"Length of '{user_input}': {len(user_input)}")

