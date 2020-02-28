dict={"k1":{"k11":{"k111":{"k1111":1}}},"k2":{"k22":{"k222":2}},"k3":{"k33":3},"k4":4}
print(type(dict))
output = {}
def nesting(dict):
    for i in dict:
        if type(dict.items()) == dict:
            nesting(i)
        else:
            output.update(i)
print ('The original dict: ', dict)
nesting(dict)
print ('The dict after removing nesting: ', output)
