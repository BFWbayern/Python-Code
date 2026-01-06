from game import Game, resetColor
import logging

APP_NAME = "Guess the number"

resetColor()

if (__name__ == "__main__"):
    print(f"Starting {APP_NAME}.\n")
    Game().run()
else:
    logging.info(f"{APP_NAME} cannot be imported as a module.")
