import random

from ui_calculator import UI
OPTIONS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', '(', ')', '-', '+', '*', '/', '^', '@', '$', '&',
           '%', '~', '!', '#']


def main():
    UI.opening_explain()
    print("\nCome on! enter your first equation.")
    equation = input()
    while equation != "exit":
        if equation == "help":
            UI.full_explain()
        else:
            try:
                UI.check_result(equation)
            except Exception:
                print("The equation you entered isn't valid.")
        print('\nEnter another equation to check its result! ("exit" to exit and "help" for explanation)')
        equation = input()


if __name__ == '__main__':
    main()
