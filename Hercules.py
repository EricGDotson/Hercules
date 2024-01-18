# Opening config Java Script Object Notation (json) file
import json
import socket

try:
    with open("config.json", "r") as f:
        data = json.load(f)
        print(data)
except FileNotFoundError:
    print("Error: File not found.")
    exit

'''
create socket
AF_INET - address family, where host is a string representing either a hostname in internet domain notation like (default)
SOCK_STREAM - Defualt socket type streaming 
'''
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Defines host
host = '192.168.10.100'
port = 1001
# do I need port?

try:
    socket.bind((host, port))
except:
    print("Can not bind to port")
    exit()


'''
    Bind to {port}
    If fail exit

    Give HTTP response of "Hello {name} today is {day}"


exit
'''
