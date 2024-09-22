#main.py

def say_hello(): #Returns a string
    return "Hello, World!"

if __name__ == "__main__":
    assert say_hello() == "Hello, World!"
    print(say_hello())
