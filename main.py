from ui_calculator import UI


def main():
    UI.opening_explain()
    print("\nCome on! enter your first equation.")
    equation = input()
    while equation != "exit":
        if equation == "help":
            UI.full_explain()
        else:
            UI.check_result(equation)
        print('\nEnter another equation to check its result! ("exit" to exit and "help" for explanation)')
        equation = input()


if __name__ == '__main__':
    main()
