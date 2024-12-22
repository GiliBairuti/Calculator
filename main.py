from utils.ui_calculator import UI


def main():
    try:
        UI.opening_explain()
        equation = UI.input_equation()
        while equation != "exit":
            if equation == "help":
                UI.full_explain()
            else:
                UI.check_result(equation)
            print('\nEnter another equation to check its result! ("exit" to exit and "help" for explanation)')
            equation = UI.input_equation()
        print("Bye bye!")
    except KeyboardInterrupt:
        print("\nThe program was forcefully closed.")


if __name__ == '__main__':
    main()
