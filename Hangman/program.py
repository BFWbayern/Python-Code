import random
import os
from console_renderer import Renderer

class Game:
    def __init__(self) -> None:
        self.header = ""
        self.footer = "Please enter your guess."
        self.is_running = False
        self.game_over = False
        self.won = False
        self.words = ["Testsubjekt", "Willkürlich", "Sinnlos", "Zufällig"]
        self.index = random.randint(0, len(self.words)-1)
        self.word = self.words[self.index]
        self.discovered:list[str] = []
        self.wrong_guesses:list[str] = []
    
    def my_render(self):
        THE_WORD = "The word: "
        MAX_WIDTH = len(THE_WORD) + len(self.word)*2
        renderer = Renderer(MAX_WIDTH, 5)
        renderer.set_cursor(0,0)
        renderer.put("a")
        renderer.set_cursor(1,1)
        
        renderer.insert("cde")
        renderer.put("a")
        renderer.put("c")
        print(renderer.to_str())

    def render(self):
        out = f"{self.header}\n"
        THE_WORD = "The word: "
        out += THE_WORD
        i = len(THE_WORD) - 1
        for char in self.word:
            if (self.discovered.__contains__(char.lower())):
                out += f"{char} "
            else:
                out += "_ "
            i += 2
        out += "   ┌─────────┐"
        
        MAX_WIDTH = i
        out += "\n" + ("━" * i) + "\n"
        youve_tried = "You've tried: "
        i = len(youve_tried)
        if(len(self.wrong_guesses) > 0):
            last_disc = self.wrong_guesses[-1]
            for disc in self.wrong_guesses:
                if(i >= MAX_WIDTH):
                    youve_tried+="\n"
                    i=0
                youve_tried += disc
                if(disc != last_disc):
                    youve_tried += ", "
                    i+=3
                else:
                    i+=1
        else:
            youve_tried += "..."
        out +=youve_tried
        os.system('cls')
        print(f"{out}\n{self.footer}")
# ┏━━━┑
# ┃   O
# ┃  /│\
# ┃  / \
#━┻━
    def request(self):
        in_ = input().lower()
        if(len(in_) < 1 or len(in_) > 1):
            self.header="Please enter one character."
        elif(self.discovered.__contains__(in_)):
            self.header="You already discovered this one."
        elif(self.wrong_guesses.__contains__(in_)):
            self.header="You already know that's not the right one."
        elif(self.word.lower().__contains__(in_)):
            self.discovered.append(in_)
            self.header= ""
        else:
            self.wrong_guesses.append(in_)
            self.header="Wrong guess."

    def is_won(self) -> bool:
        for char in self.word:
            if (not self.discovered.__contains__(char.lower())):
                return False
        return True

    def run(self):
        self.is_running = True
        while((self.is_running)):
            self.render()
            if(len(self.wrong_guesses) > 9):
                self.game_over = True
            if(self.is_won()):
                self.game_over = True
                self.won = True
                print("Won!")
            if(self.game_over):
                break
            self.request()
        self.render()
            
game = Game()
#game.run()
game.my_render()