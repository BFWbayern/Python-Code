def tannenbaum(ebenen: int) -> str:
    output : list[str] = []
    for i in range(ebenen):
        output.append(' '*(ebenen - 1 - i) + '*'*(i*2 + 1))
    output.append(' '*(ebenen - 1) + '|')
    return '\n'.join(output)

if __name__ == "__main__":
    while (True):
        eingabe = int(input("Ebenenzahl: "))
        print(tannenbaum(eingabe))
