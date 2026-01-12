def aufgabe01():
    print("Hey, World!")

def aufgabe02():
    print("Hey, ", 42)

def aufgabe03():
    a = 5
    print(type(a))

def aufgabe04():
    b = 3.14
    print(type(b))

def aufgabe05():
    c = "Hallo"
    print(type(c))

def aufgabe06():
    d = True
    print(type(d))

def aufgabe07():
    a = 3
    print(a + 4)

def aufgabe08():
    a = 3
    print(a - 4)

def aufgabe09():
    a = 2
    print(a * 3)

def aufgabe10():
    a = 10
    a = a / 2
    print(a)

def aufgabe11():
    a = 7
    b = 2
    print(round(a / b, 1))

def aufgabe12():
    a = 11
    print(a % 3)

def aufgabe13():
    a = "Hallo"
    b = "Python"
    print(a + "+" + b)

def aufgabe14():
    x = "10"
    print(x * 2)
    print(int(x) * 2)

def aufgabe15():
    a = 5
    b = 5
    print(a >= b)

def aufgabe16():
    a = True
    b = False
    print(a or b and not b)

def aufgabe17():
    for i in range(2, 5):
        print(i)

def aufgabe18():
    print(type(5.0) == float)

def aufgabe19():
    x = 0
    while x < 3:
        print("x =", x)
        x += 1

def aufgabe20():
    for i in range(5):
        if i == 3:
            break

def aufgabe21():
    c = 3
    for z in range(0, c):
        print(z)

def aufgabe22():
    t = "abc"
    for b in t:
        print(b)

def aufgabe23():
    a = False
    print(not a)

def aufgabe24():
    a = False
    print(not (not a))

def aufgabe25():
    text = "abcdef"
    print(text[0])

def aufgabe26():
    {
    # print("abcdef".[-1])
    }

def aufgabe27():
    a = 3
    a = a + 3
    a += 3
    print(a)

def aufgabe28():
    a = "Hi"
    print(a * 3)

def aufgabe29():
    a = "abc"
    print(a.upper())

def aufgabe30():
    print("TeXT".lower())

def aufgabe31():
    s = ""
    x = [51+52]+[222//2]*2+[50*2]
    for i in x:
        if i % 2 == 0 or i > 100:
            s += chr(i)
    print(s)

def aufgabe32():
    d = ['!',"1","I","0","5","2","T"]
    print(d[5] + d[4] + d[3] + d[1])
