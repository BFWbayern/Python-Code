def get_whitespace_list(length: int) -> list[str]:
    return [' ' for _ in range(length)]

class Renderer:
    def __init__(self, width: int, height: int) -> None:
        self.buffer = get_whitespace_list(width * height)
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def to_str(self) -> str:
        output = ""
        for i in range(0, len(self.buffer)):
            if(i >= self.width and i % self.width == 0):
                output += "\n"
            output += self.buffer[i]
            
        return output.rstrip()
    
    def set_cursor(self, x: int, y: int):
        if x >= self.width:
            new_row = x // self.width
            x = x - self.width * new_row
            y = y + new_row
        if y >= self.height:
            raise Exception("The rendering buffer is too small.")
        self.x = x
        self.y = y

    def put(self, char: str):
        if type(char) is not str:
            char = str(char)
        if len(char) != 1:
            raise Exception(f"Parameter 'char' must be of length 1, actual length: {len(char)}.")
        index = self.x + self.y * self.width
        if index >= len(self.buffer):
            raise Exception("The rendering buffer is too small.")

        self.buffer[index] = char
        self.indent()

    def put_for(self, char: str, length: int):
        for _ in range(length):
            self.put(char)

    def insert(self, text: str):
        for char in text:
            self.put(char)

    def indent(self, i: int = 1):
        self.set_cursor(self.x + i, self.y)
