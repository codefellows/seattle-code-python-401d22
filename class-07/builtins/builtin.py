import builtins

_print = builtins.print
_input = builtins.input

def alter():
    builtins.print = _input
    builtins.input = _print


def alter_back():
    builtins.print = _print
    builtins.input = _input


alter()
print('What is your name?')


alter_back()
print('What is your name?')
