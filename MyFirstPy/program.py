app_name = "MyFirstPy"

if __name__ == '__main__':
    print(f"App '{app_name}' started.\n")
else:
    raise Exception(f"{__name__} cannot be imported as a module.")

print("Hello, world")