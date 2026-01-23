import random
import os
import time
from console_renderer import Renderer

THE_WORD = "The word: "

class Game:
    def __init__(self) -> None:
        self.is_running = False
        self.won = False
        self.words = ["Testsubjekt", "Willkuerlich", "Sinnlos", "Zufaellig"]
        self.index = random.randint(0, len(self.words)-1)
        self.word = self.words[self.index]
        self.discovered:list[str] = [self.word[random.randint(0, len(self.word)-1)].lower()]
        self.wrong_guesses:list[str] = []
        self.MAX_WIDTH = len(THE_WORD) + len(self.word)*2+3
        self.MAX_HEIGHT = 7
    
    def renderer(self):
        renderer = Renderer((self.MAX_WIDTH)*2, self.MAX_HEIGHT)
        self._render_box(renderer)
        self._render_guess_screen(renderer)
        self._render_hangman_screen(renderer)
        os.system('cls')
        print(renderer.to_str())

    def _render_box(self, renderer: Renderer):
        renderer.put('╔')
        renderer.put_for('═', self.MAX_WIDTH-2)
        renderer.put('╦')
        renderer.put_for('═', self.MAX_WIDTH-2)
        renderer.put('╗')
        
        for i in range(1,self.MAX_HEIGHT):
            renderer.set_cursor(0, i)
            renderer.put('║')
            renderer.set_cursor(self.MAX_WIDTH-1, i)
            renderer.put('║')
            renderer.set_cursor(self.MAX_WIDTH*2-2, i)
            renderer.put('║')
        
        renderer.set_cursor(0,self.MAX_HEIGHT-1)
        renderer.put('╚')
        renderer.put_for('═', self.MAX_WIDTH-2)
        renderer.put('╩')
        renderer.put_for('═', self.MAX_WIDTH-2)
        renderer.put('╝')
    
    def _render_guess_screen(self, renderer: Renderer):
        renderer.set_cursor(2,1)
        renderer.insert("The word: ")
        i = len(THE_WORD) - 1
        for char in self.word:
            if (self.discovered.__contains__(char.lower())):
                renderer.insert(char+ ' ')
            else:
                renderer.insert("_ ")
            i += 2

        WRONG_GUESSES_STR = "Wrong guesses: "
        i = len(WRONG_GUESSES_STR)
        y = 2
        renderer.set_cursor(2, y)
        renderer.insert(WRONG_GUESSES_STR)
        if(len(self.wrong_guesses) > 0):
            last_disc = self.wrong_guesses[-1]
            for disc in self.wrong_guesses:
                if(i >= self.MAX_WIDTH-2-3):
                    y += 1
                    renderer.set_cursor(2,y)
                    i=0
                renderer.insert(disc)
                i+=1
                if(disc != last_disc):
                    renderer.insert(", ")
                    i+=2
        else:
            renderer.put_for('.', 3)

    def _render_hangman_screen(self, renderer: Renderer):
        wrong_count = len(self.wrong_guesses)
        if(wrong_count < 1):
            return
        renderer.set_cursor(int(self.MAX_WIDTH*1.5-4), self.MAX_HEIGHT-2)
        renderer.insert('━┻━')
        if(wrong_count < 2):
            return
        renderer.set_cursor(renderer.x-2,renderer.y-1)
        renderer.put('┃')
        if(wrong_count < 3):
            return
        renderer.set_cursor(renderer.x-1,renderer.y-1)
        renderer.put('┃')
        if(wrong_count < 4):
            return
        renderer.set_cursor(renderer.x-1,renderer.y-1)
        renderer.put('┃')
        renderer.set_cursor(renderer.x-1,renderer.y-1)
        renderer.put('┏')
        if(wrong_count<5):
            return
        renderer.insert('━━')
        if(wrong_count<6):
            return
        renderer.insert('━┑')
        if(wrong_count < 7):
            return
        renderer.set_cursor(renderer.x-1,renderer.y+1)
        renderer.put('0')
        if(wrong_count<8):
            return
        renderer.set_cursor(renderer.x-2,renderer.y+1)
        renderer.insert('/│\\')
        if(wrong_count<9):
            return
        renderer.set_cursor(renderer.x-3,renderer.y+1)
        renderer.insert('/ \\')

    def is_won(self) -> bool:
        for char in self.word:
            if (not self.discovered.__contains__(char.lower())):
                return False
        return True

    def request(self):
        user_input = input("Eingabe: ").lower()
        if(len(user_input)!=1):
            self.renderer()
            print("Bitte geben Sie einen Buchstaben ein.")
            return self.request()
        char = user_input[0]
        val = ord(char)
        if(not(val > 64 and val < 91 or val > 96 and val < 123)):
            self.renderer()
            print("Eingabe war kein Buchstabe. Bitte erneut versuchen.")
            return self.request()
        if(char in self.word.lower()):
            if(not (char in self.discovered)):
                self.discovered.append(char)
                return
            else:
                self.renderer()
                print("Der ist schon entdeckt.")
                return self.request()
        if(char in self.wrong_guesses):
            self.renderer()
            print("Wir wissen schon, der ist es nicht.")
            return self.request()
        self.wrong_guesses.append(char)
        return
        
    def run(self):
        self.is_running = True
        while((self.is_running)):
            self.renderer()
            self.request()
            if(len(self.wrong_guesses) == 9):
                self.is_running = False
            if(self.is_won()):
                self.is_running = False
                self.won = True
            if(not self.is_running):
                break
            time.sleep(0.25)
        self.renderer()
        if(self.won):
            print("Gewonnen!")
        else:
            print("Verloren!")

if(not (__name__ == "__main__")):
    raise Exception("The module cannot be imported.")

game = Game()
game.run()
