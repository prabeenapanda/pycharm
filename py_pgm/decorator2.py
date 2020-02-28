def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")
#******************************
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Hello
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#******************************


@percent
@star
def printing(msgs):
    print(msgs)
printing("hi")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#******************************
#hi
#******************************
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%