from helpers.io_helper import request_input

def aufgabe01():
    print("Hello, World!")

def aufgabe02():
    print("Wie ist dein Vorname?")
    vorname = input()
    print(f"Hallo, {vorname}")

def aufgabe03():
    num = 3.1415
    print(f"{num}: {type(num)}")

def aufgabe04():
    text = 10
    textAsInt = int(text)
    textAsFloat = float(text)
    print(f"{textAsInt=}")
    print(f"{textAsFloat=}")

def aufgabe05():
    num = 3.1415
    print(round(num, 2))

def aufgabe06():
    user_input = request_input()
    print(f"{user_input}: {type(user_input)}")

def aufgabe07():
    user_input = request_input()
    print(f"Length of '{user_input}': {len(user_input)}")

def aufgabe08():
    print(f"0 as bool: {bool(0)}")
    print(f"1 as bool: {bool(1)}")
    print(f"\"\" as bool: {bool("")}")
    print(f"\"abc\" as bool: {bool("abc")}")
    print(f"None as bool: {bool(None)}")

def aufgabe09():
    val = 3.1415
    if(type(val) is float):
        print("Ja, ist float.")
    else:
        print("Nein, ist kein float.")

def aufgabe10():
    val = 3 + 2 * 4 - 5
    print(val)

def aufgabe11():
    num1 = 3546
    num2 = 24353
    print(f"{num1}+{num2}= {num1+num2}")
    print(f"{num1}-{num2}= {num1-num2}")
    print(f"{num1}*{num2}= {num1*num2}")
    print(f"{num1}/{num2}= {num1/num2}")

def aufgabe12():
    min = 135
    hours = min // 60
    min -= hours * 60 # or, min % hours % 60
    print(f"{hours} Stunden, {min} Minuten.")

def aufgabe13():
    user_input = input("Geben Sie eine Zahl an: ")
    try:
        zahl = float(user_input)
        print(zahl * 2)
    except ValueError:
        print("Dies war gar keine Zahl :(")

def aufgabe14():
    a = 3
    a += 3
    print(a)

def aufgabe15():
    user_input = input("Geben Sie eine Zahl an: ")
    try:
        zahl = float(user_input)
        if zahl % 2 == 0:
            print("Die Zahl ist gerade.")
        else:
            print("Die Zahl ist ungerade.")
    except ValueError:
        print("Dies war gar keine Zahl :(")
    
def aufgabe16():
    user_input = input("Geben Sie eine Zahl an: ")
    try:
        zahl = float(user_input)
        if zahl % 2 == 0 and zahl % 3 == 0:
            print("Die Zahl ist durch 2 teilbar (gerade) UND durch 3 teilbar.")
        else:
            print("Die Zahl ist nicht durch 2 UND durch 3 gleichzeitig teilbar.")
    except ValueError:
        print("Dies war gar keine Zahl :(")

def aufgabe17():
    val1 = 2343
    val2 = 2342

    if(val1 > val2):
        print(f"{f"val1=".split("=")[0]} ist größer.")
    elif val1 < val2:
        print(f"{f"val2=".split("=")[0]} ist größer.")
    else:
        print(f"{f"val1=".split("=")[0]} und {f"val2=".split("=")[0]} sind gleich groß.")

def aufgabe18():
    str1, str2 = "Hallo", "Welt"
    concat = str1 + "-" + str2
    print(concat)

def aufgabe19():
    string = "hALLo"
    lower = string.lower()
    upper = string.upper()

def aufgabe20():
    string = "wurstbrot"
    print(string[0]+", "+string[-1])

def aufgabe21():
    string = "wurstbrot"
    for c in string:
        print(c)

def aufgabe22():
    string = "Programmieren"
    print(string[-3])

def aufgabe23():
    print(True and not False)

def aufgabe24():
    a = True
    not_a = not a
    print(not_a)

def aufgabe25():
    user_input = input("Geben Sie eine Zahl an: ")
    try:
        zahl = float(user_input)
        if zahl > 0:
            print("Die Zahl ist größer als null.")
        elif zahl < 0:
            print("Die Zahl ist kleiner als null.")
        else:
            print("Die Zahl ist null.")
    except ValueError:
        print("Dies war gar keine Zahl :(")
    
def aufgabe26():
    user_input = input("Geben Sie Ihr Alter an: ")
    try:
        zahl = int(user_input)
        if zahl > 17:
            print("Sie sind volljährig.")
        else:
            print("Du bist noch ein Kind.")
    except ValueError:
        print("Dies war gar keine Zahl :(")

def aufgabe27():
    for i in range(0, 9 + 1):
        print(i, end = ', ')

def aufgabe28():
    for i in range(0, 42 + 1):
        print(i, end = ', ')

def aufgabe29():
    for i in range(0, 42 + 1):
        if(i%2==0):
            print(i, end = ', ')

def aufgabe30():
    user_input = input("Geben Sie eine Zahl über 0 an: ")
    try:
        zahl = int(user_input)
        if zahl > 0:
            for i in range(0, zahl + 1):
                print(i, end = ', ')
        else:
            print("Die Zahl ist kleiner als oder gleich null.")
    except ValueError:
        print("Dies war gar keine Zahl :(")

def aufgabe31():
    while True:
        user_input = input("Geben Sie eine Zahl an: ")
        try:
            zahl = int(user_input)
            if zahl is not 0:
                print("Probieren Sie's weiter.")
            else:
                print("Juppi.")
                break
        except ValueError:
            print("Dies war gar keine Zahl :(")

def aufgabe32():
    while True:
        user_input = input("Geben Sie einen Namen ein: ")
        if(user_input is not "Wilfried"):
            "Probieren Sie's weiter."
        else:
            print("Der ist es.")
            break

def aufgabe33():
    zahlen = [1, 2, 3, 4]
    print(f"Zweites Element: {zahlen[1]}, Länge: {len(zahlen)}")

def aufgabe34():
    dict = {
        "name": "Wilfried",
        "alter": 25
    }

def aufgabe35():
    set = {"rot", "grün", "blau"}
    set.add("gelb")

def aufgabe36():
    tuple = ("Montag", "Dienstag", "Mittwoch")

def aufgabe37():
    liste = [1, 2, 2, 3, 4, 4, 4]
    ohne_duplikate = list(set(liste))

def begruesse():
    print("Hallo, willkommen")

def quadrat(zahl: int):
    print(zahl * zahl)

def ist_gerade(zahl: int):
    return(zahl % 2 == 0)

def ist_ungerade(zahl: int):
    return(zahl % 2 != 0)

def addiere(zahl1: int, zahl2: int):
    return zahl1 + zahl2
