def is_palindrome(text: str) -> bool:
    for i in range(0, len(text)//2):
        end = len(text)-1-i
        if(text[i] != text[end]):
            return False
        if(i == end):
            break
    return True

def char_commonness(text: str) -> dict[str, int]:
    chars: dict[str, int] = {}
    for i in text:
        if i in chars:
            v = chars[i]
            chars[i] = v + 1
        else:
            chars[i] = 1
    return chars

while(True):
    user_input = input("Please enter something, or q to quit: ")
    
    if(user_input == 'q'):
        break

    if(is_palindrome(user_input)):
        print("Input is considered a palindrome.")
    else:
        print("Input is not a palindrome")

    print("Char commonness:")
    print(char_commonness(user_input))