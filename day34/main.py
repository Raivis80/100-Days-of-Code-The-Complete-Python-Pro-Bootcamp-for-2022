# Type hints are optional, but they are a good practice

def main(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False

print(main(18))

# Path: day34\main.py