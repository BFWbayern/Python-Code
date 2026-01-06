from colors import ColorCodes
import random
import sys
import os

MIN_VALUE = 1
MAX_VALUE = 100
QUIT_KEY = 'q'

def setColor(color: ColorCodes) -> None:
    """
    Sets the currently used color.
    
    :param color: The color to use.
    :type color: ColorCodes
    """
    sys.stdout.write(color.value)

def resetColor() -> None:
    """
    Resets the color to the default one.
    """
    setColor(ColorCodes.DEFAULT)

def clear():
    """
    Clears the screen.
    """
    os.system('cls')

def output(text: str, color: ColorCodes = ColorCodes.DEFAULT) -> None:
    """
    Prints the specified text using the specified color.\n
    Resets the color after printing.

    :param text: The text to be printed.
    :type text: str
    :param color: The color to use.
    :type color: ColorCodes
    """
    print(f"{color.value}{text}{ColorCodes.DEFAULT.value}")

def prompt(color: ColorCodes = ColorCodes.YELLOW) -> str:
    """
    Prompts the user for an input.\n
    Sets the color the user writes in to the specified color, resets the color after the input.
    
    :param color: The color to use.
    :type color: ColorCodes
    :return: The user input.
    :rtype: str
    """
    setColor(color)
    user_input = input()
    resetColor()
    return user_input

class Game:
    """
    Represents the main class for the game logic.
    """
    is_running = False

    def run(self):
        """
        Starts the game loop.
        
        :param self: The game instance.
        """
        is_running = True

        while (is_running):
            num = random.randint(MIN_VALUE, MAX_VALUE)
            output(f"Guess the integer number between {MIN_VALUE} and {MAX_VALUE}.")

            while (True):
                user_input = prompt()

                try:
                    guess = int(user_input)

                    if (guess < MIN_VALUE):
                        output(f"Your number was smaller than {MIN_VALUE}. Please enter a integer between {MIN_VALUE} and {MAX_VALUE}.", ColorCodes.RED)
                        continue
                    elif (guess > MAX_VALUE):
                        output(f"Your number was bigger than {MAX_VALUE}. Please enter a integer between {MIN_VALUE} and {MAX_VALUE}.", ColorCodes.RED)
                        continue
                    
                    if (guess < num):
                        output("Your number is too small. Try again :)")
                    elif (guess > num):
                        output("Your number is too big. Try again...")
                    else:
                        output(f"You nailed it!{ColorCodes.DEFAULT.value}\nTo reroll, just hit enter; to quit, hit anything else.", ColorCodes.GREEN)
                        
                        if (prompt(ColorCodes.CYAN) != ''):
                            is_running = False
                            return
                        clear()
                        break
                except:
                    if (len(user_input) == 1 and user_input[0].lower() == QUIT_KEY):
                        is_running = False
                        output("We're stopping right 'ere.\nBye.", ColorCodes.BOLD)
                        return
                    output("Your input was not in the format of an integer. Please re-enter.", ColorCodes.RED)
                    continue
