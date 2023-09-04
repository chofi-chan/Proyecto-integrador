import os
import readchar
from readchar import key

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    number = 0
    while number <= 50:
        clear_terminal()
        print(f"Número actual: {number}")

        char = readchar.readkey()

        if char == "n":
            number += 1
            if number == 50:
                clear_terminal()
                print("¡Llegaste al número 50!")
                break

if __name__ == "__main__":
    main()
