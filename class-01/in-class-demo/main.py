def get_user_input(num=0):
    # I am in the function
    print("Please Enter your Name")
    user_name = input("> ")
    print(user_name)
    print('The user name is: ' + user_name )

    print('older')
    print('The user name is: {}'.format(user_name))

    print('newer')
    print(f'The user name is {user_name}.')

get_user_input()

if __name__ == "__main__":
    # This is outside the function
    get_user_input()
    # pass
