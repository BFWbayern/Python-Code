import random
import os
import time
from console_renderer import Renderer

THE_WORD_STR = "The word: "
THE_WORD_LEN = len(THE_WORD_STR)

class Game:
    def __init__(self) -> None:
        self.is_running = False
        self.is_won = False
        self.words = ["Testsubjekt", "Willkuerlich", "Sinnlos", "Zufaellig"]
        self.index = random.randint(0, len(self.words)-1)
        self.word = self.words[self.index]
        self.discovered: list[str] = [self.word[random.randint(0, len(self.word)-1)].lower()]
        self.wrong_guesses: list[str] = []
        self.MAX_WIDTH = THE_WORD_LEN + len(self.word)*2 + 3
        self.MAX_HEIGHT = 7
    
    def render(self) -> None:
        renderer = Renderer(self.MAX_WIDTH*2, self.MAX_HEIGHT)
        self.__render_box(renderer)
        self.__render_guess_screen(renderer)
        self.__render_hangman_screen(renderer)
        os.system("cls")
        print(str(renderer))

    def __render_box(self, renderer: Renderer) -> None:
        renderer.put('╔')
        renderer.put_for('═', self.MAX_WIDTH-2)
        renderer.put('╦')
        renderer.put_for('═', self.MAX_WIDTH-2)
        renderer.put('╗')
        
        for i in range(1, self.MAX_HEIGHT):
            renderer.set_cursor(0, i)
            renderer.put('║')
            renderer.set_cursor(self.MAX_WIDTH-1, i)
            renderer.put('║')
            renderer.set_cursor(self.MAX_WIDTH*2 - 2, i)
            renderer.put('║')
        
        renderer.set_cursor(0, self.MAX_HEIGHT-1)
        renderer.put('╚')
        renderer.put_for('═', self.MAX_WIDTH-2)
        renderer.put('╩')
        renderer.put_for('═', self.MAX_WIDTH-2)
        renderer.put('╝')
    
    def __render_guess_screen(self, renderer: Renderer) -> None:
        renderer.set_cursor(2, 1)
        renderer.insert("The word: ")
        i = THE_WORD_LEN-1

        for char in self.word:
            if(self.discovered.__contains__(char.lower())):
                renderer.insert(char + ' ')
            else:
                renderer.insert("_ ")
            i += 2

        WRONG_GUESSES_STR = "Wrong guesses: "
        i = len(WRONG_GUESSES_STR)
        y = 2

        renderer.set_cursor(2, y)
        renderer.insert(WRONG_GUESSES_STR)

        if(len(self.wrong_guesses) > 0):
            last_wrong_guess = self.wrong_guesses[-1]
            for wrong_guess in self.wrong_guesses:
                if(i >= self.MAX_WIDTH-2-3):
                    y += 1
                    i = 0
                    renderer.set_cursor(2, y)
                i += 1
                renderer.insert(wrong_guess)
                if(wrong_guess != last_wrong_guess):
                    i += 2
                    renderer.insert(", ")
        else:
            renderer.insert("...")

    def __render_hangman_screen(self, renderer: Renderer) -> None:
        wrong_guesses_count = len(self.wrong_guesses)

        if(wrong_guesses_count < 1):
            return
        renderer.set_cursor(int(self.MAX_WIDTH*1.5 - 4), self.MAX_HEIGHT-2)
        renderer.insert("━┻━")

        if(wrong_guesses_count < 2):
            return
        renderer.update_cursor(-2, -1)
        renderer.put('┃')

        if(wrong_guesses_count < 3):
            return
        renderer.update_cursor(-1, -1)
        renderer.put('┃')

        if(wrong_guesses_count < 4):
            return
        renderer.update_cursor(-1, -1)
        renderer.put('┃')
        renderer.update_cursor(-1, -1)
        renderer.put('┏')

        if(wrong_guesses_count < 5):
            return
        renderer.insert("━━")

        if(wrong_guesses_count < 6):
            return
        renderer.insert("━┑")

        if(wrong_guesses_count < 7):
            return
        renderer.update_cursor(-1, 1)
        renderer.put('0')

        if(wrong_guesses_count < 8):
            return
        renderer.update_cursor(-2, 1)
        renderer.insert('/│\\')

        if(wrong_guesses_count < 9):
            return
        renderer.update_cursor(-3, 1)
        renderer.insert('/ \\')

    def check_is_won(self) -> bool:
        for char in self.word:
            if (not self.discovered.__contains__(char.lower())):
                return False
        return True

    def request(self) -> None:
        user_input = input("Eingabe: ").lower()

        if(len(user_input) != 1):
            self.render()
            print("Bitte geben Sie einen Buchstaben ein.")
            return self.request()
        char = user_input[0]
        val = ord(char)

        if(not (val > 64 and val < 91 or val > 96 and val < 123)):
            self.render()
            print("Eingabe war kein Buchstabe. Bitte erneut versuchen.")
            return self.request()
        
        if(self.word.lower().__contains__(char)):
            if(not self.discovered.__contains__(char)):
                self.discovered.append(char)
                return
            else:
                self.render()
                print("Der ist schon entdeckt.")
                return self.request()
            
        if(self.wrong_guesses.__contains__(char)):
            self.render()
            print("Wir wissen schon, der ist es nicht.")
            return self.request()
        self.wrong_guesses.append(char)
        return
        
    def run(self) -> "Game":
        if(self.is_running):
            raise Exception("The game is already running.")
        
        self.is_running = True

        while(self.is_running):
            self.render()
            self.request()

            if(len(self.wrong_guesses) == 9):
                self.is_running = False
                self.is_won = False

            if(self.check_is_won()):
                self.is_running = False
                self.is_won = True

            if(not self.is_running):
                break
            time.sleep(0.25)
        self.render()

        if(self.is_won):
            print("Gewonnen!")
        else:
            print("Verloren!")

        return self

if(not __name__ == "__main__"):
    raise Exception(f"The module \"{__name__}\" cannot be imported.")

game = Game().run()
