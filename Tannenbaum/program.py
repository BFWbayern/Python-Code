def tannenbaum(ebenen: int) -> None:
    max = 2*ebenen - 1
    half_max = max // 2
    output = ""
    for i in range(ebenen):
        j = half_max -i
        output += ' ' * j
        ii = half_max-j+i+1
        output += '*' * ii
        output += '\n'
    output += ' ' * half_max + '|'
    print(output)

if __name__ == "__main__":
    while (True):
        eingabe = int(input("Ebenenzahl: "))
        tannenbaum(eingabe)
        