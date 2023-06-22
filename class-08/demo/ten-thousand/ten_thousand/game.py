from sys import exit


def play():
    pass


def main():
    name = input("Please Enter your name: ")
    while True:
        user_answer = input(f'{name}, please enter q to quit ')
        if user_answer == 'q':
            quit_game('Thank you for following directions')


def quit_game(message):
    exit(message)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit_game('KeyBoard Interrupt Detected')

