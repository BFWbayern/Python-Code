def get_whitespace_list(length: int) -> list[str]:
    return [' ' for _ in range(length)]

class Renderer:
    def __init__(self, width: int, height: int) -> None:
        self.__buffer = get_whitespace_list(width*height)
        self.__x = 0
        self.__y = 0
        self.__width = width
        self.__height = height

    def to_str(self) -> str:
        output = ""

        for i in range(0, len(self.__buffer)):
            if(i >= self.__width and i % self.__width == 0):
                output += '\n'
            output += self.__buffer[i]
        return output.rstrip()
    
    def __str__(self):
        return self.to_str()

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y
    
    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height
    
    def set_cursor(self, x: int, y: int) -> None:
        if(x >= self.__width):
            new_row = x // self.__width
            x = x - self.__width*new_row
            y = y + new_row

        if(y >= self.__height):
            raise Exception("The rendering buffer is too small.")
        self.__x = x
        self.__y = y

    def update_cursor(self, x: int, y: int) -> None:
        self.set_cursor(self.__x+x, self.__y+y)

    def put(self, char: str) -> None:
        if(type(char) is not str):
            char = str(char)

        if(len(char) != 1):
            raise Exception(f"Parameter 'char' must be of length 1, actual length: {len(char)}.")
        index = self.__x + self.__y*self.__width

        if(index >= len(self.__buffer)):
            raise Exception("The rendering buffer is too small.")
        self.__buffer[index] = char
        self.indent()

    def put_for(self, char: str, length: int) -> None:
        for _ in range(length):
            self.put(char)

    def insert(self, text: str) -> None:
        for char in text:
            self.put(char)

    def indent(self, i: int = 1) -> None:
        self.set_cursor(self.__x + i, self.__y)
