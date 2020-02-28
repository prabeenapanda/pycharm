import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    message = input("Please enter a number to check prime or not: ")
    while message != 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("From Server: " + data)
        message = input("Please enter a number to check prime or not: ")

    s.close()

if __name__ == '__main__':
    Main()
    
    
    
