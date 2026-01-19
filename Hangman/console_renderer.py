class Renderer:
    def __init__(self, width) -> None:
        self.buffer = [' ' for _ in range(width * 5)]
        self.x = 0
        self.y = 0
        self.width = width

    def to_str(self) -> str:
        output = ""
        for i in range(0, len(self.buffer)):
            if(i >= self.width and i % self.width == 0):
                output += "\n"
            output += self.buffer[i]
            
        return output.rstrip()
    
    def set_cursor(self, x: int, y: int):
        if(x >= self.width):
            rr = x // self.width
            x = x - self.width
            y = y + rr
            new_i = x + y * self.width
            if(new_i >= len(self.buffer)):
                self.buffer += [' ' for _ in range(new_i-len(self.buffer))]
        self.x = x
        self.y = y

    def put(self, char: str):
        if(len(char) < 1 or len(char) > 1):
            raise Exception("Char must have a length of 1.")
        
        i: int = self.x + self.y * self.width
        self.buffer[i] = char
    
    def insert(self, text: str):
        for char in text:
            self.put(char)
            self.indent()

    def indent(self, i: int = 1):
        self.set_cursor(self.x + i, self.y)
    