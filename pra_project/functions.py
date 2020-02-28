

def input_int(message):
    """
Test
    """
    input_val = ""
    while not input_val.isnumeric():
        input_val = input(message)
    return int(input_val)
print(input_int("32541"))
