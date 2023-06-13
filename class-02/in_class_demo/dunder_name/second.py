import first

first.print_me_from_first()

def print_me_from_second():
    print(f'Second Module: {__name__}')

if __name__ == '__main__':
    print_me_from_second()
