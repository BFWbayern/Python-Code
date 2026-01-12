from importlib import import_module
from inspect import getmembers, isfunction

class ModuleReflector:
    def __init__(self, module_name):
        self.module_name = module_name

    def get_functions(self):
        module = import_module(self.module_name)
        functions = [
            func for name, func in getmembers(module, isfunction)
            if (func.__module__ == module.__name__)
        ]
        return functions
