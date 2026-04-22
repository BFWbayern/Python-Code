def tannenbaum(ebenen: int) -> str:
    output : list[str] = []
    for i in range(ebenen):
        output.append(' '*(ebenen - 1 - i) + '*'*(i*2 + 1))
    output.append(' '*(ebenen - 1) + '|')
    return '\n'.join(output)

if __name__ == "__main__":
    while (True):
        user_input = input("Ebenenzahl oder q: ")
        try:
            ebene = int(user_input)

            if(ebene < 1):
                print("Bitte geben Sie eine Ganzzahl größer als 0 ein.")
                continue
            print(tannenbaum(ebene))
        except ValueError:
            if(len(user_input) == 1 and (user_input[0] == 'q' or user_input[0] == 'Q')):
                break
            print("Eingabe war keine Ganzzahl.")
