import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket() # creatting a TCP Socket Object
    s.bind((host, port))
    
    s.listen(1) # listen to 1 connection at a time
    print("Server started...")
    c, addr = s.accept() # Accept the connection from client, c--> client, addr--> ip address
    print("Connection form: " + str(addr))

    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From Connected user: " + data)
        try:
            if is_prime(int(data)):
                msg = 'The input number is prime'
            else:
                msg = 'The input number is not prime'
        except ValueError:
            msg = 'Please enter a numeric value'
        c.send(msg.encode('utf-8'))
    c.close()

def is_prime(inpt):
    return (True if inpt % 2 == 0 else False)

if __name__ == '__main__':
    Main()




