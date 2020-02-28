def power(voltage, state='state', action='action', type='type'):
    print ("VOLTAGE = ", voltage)
    print ("STATE   = ", state)
    print ("ACTION  = ", action)
    print ("TYPE    = ", type)

power(1000)                                         # 1 positional argument
print("------------------------------------------")
power(voltage=1000)                                  # 1 keyword argument
print("------------------------------------------")
power(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
print("------------------------------------------")
#power(action='VOOOOOM', 1000000)             # 2 keyword arguments positional arg follows keyword so error
print("------------------------------------------")
power('a million', 'bereft of life', 'jump')         # 3 positional arguments
print("------------------------------------------")
power('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
print("------------------------------------------")

""" Below are invalid """
#power()                     # required argument missing
#power(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument pos arg follow keyword so error
#power(110, voltage=220)     # duplicate value(argument) for the same parameter multiple values for voltage err
#power(actor='John Cleese')  # unknown keyword argument error


