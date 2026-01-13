from abc import ABC, abstractmethod
import sys

class Command(ABC):
    registry: list[type] = []

    @classmethod
    def register(cls, subcls: type):
        cls.registry.append(subcls)
        return subcls
    
    @classmethod
    def create_all(cls) -> list["Command"]:
        return [subcls() for subcls in cls.registry]
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls is not Command:
            Command.registry.append(cls)

    def __init__(self, name: str, params: list[str] = []):
        self.name = name
        self.params = params

    @abstractmethod
    def execute(self, args: list[str] = []):
        ...

class SwitchModeCommand(Command):
    MODES = ["aufgaben", "ausgabeanalyse"]

    def __init__(self):
        super(SwitchModeCommand, self).__init__("switch", ["mode"])
        self.current_mode = 0

    def _switch_mode(self):
        self._set_mode(self.current_mode + 1)

    def _set_mode(self, val):
        if(val >= len(SwitchModeCommand.MODES)):
            val = len(SwitchModeCommand.MODES) - 1
        elif(val < 0):
            val = 0
        self.current_mode = val

    def execute(self, args: list[str] = []):
        if(len(args) > len(SwitchModeCommand.MODES)):
           raise Exception(f"Switch command allows a maximum of {len(SwitchModeCommand.MODES)} arguments.")
        
        if(len(args) is 0):
            self._switch_mode()
        else:
            try:
                mode = int(args[0])
                self._set_mode(mode)
            except ValueError:
                raise Exception("Switch command expects an integer argument.")
            
        return SwitchModeCommand.MODES[self.current_mode]

class ExitCommand(Command):
    def __init__(self):
        super(ExitCommand, self).__init__("exit")

    def execute(self, args: list[str] = []):
        print("Programm wurde beendet.")
        sys.exit()
