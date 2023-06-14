# print("let's do something totally wrong. See if you can spot me in the output!")
# print("Too many parentheses"))
#
# print("More wrongness. Do I get printed?")
# print("Who has ever "messed up" quotations marks?")

# print("What happens now? Do you see me printed?")
# value = 1/0

# try:
#     print("Divide by zero again", 1 / 0)
# except ZeroDivisionError:
#     print("Don't divide by zero silly.")
#
# print("handled the exception above, carrying on")


# try:
#     print("Divide by zero again", 1 / "spam")
# except:
#     print("Don't divide by zero silly.")
#
# print("Total lie! The problem was not dividing by zero. It was a type error")
#
# try:
#     spam = 40 / 0
# # except ZeroDivisionError:
# #     print("Don't divide by zero silly.")
# except Exception as e:  # notice we can refer to the exception using 'as'
#     print(e)
#     print("So sorry end user. Something broke!")

# print("Attempting to create message")
# try:
#     message = "nothing " + "wrong " + "here"
# except TypeError:
#     print("Unable to create message")
# except ZeroDivisionError:
#     print("Cannot divide by 0")
# finally:
#     print("Message successfully created.......")

age = 20
if age < 21:
    raise ValueError("Invalid Age: Must be 21")

