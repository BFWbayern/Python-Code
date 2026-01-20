from sys import maxsize

def addieren(a: int, b: int) -> int:
    s = a + b
    return s

a = 10
b = 20
summe = addieren(a, b)
print(summe)

# ---

def my_min(liste: list[int]) -> int:
    min = maxsize
    for i in liste:
        if i < min:
            min = i
    return min

daten = [10, 500, 3]
print(my_min(daten))
