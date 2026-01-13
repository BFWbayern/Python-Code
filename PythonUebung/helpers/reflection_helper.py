from importlib import import_module
from inspect import getmembers, isfunction

class ModuleReflector:
    def __init__(self, module_name):
        self.module = import_module(module_name)

    def get_functions(self): 
        functions = [
            func for name, func in getmembers(self.module, isfunction)
            if (func.__module__ == self.module.__name__)
        ]
        return functions
