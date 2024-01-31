import os
import json
import time
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler

# TODO:
# put config in gitignore
# grabbing ip from vpn and not joan

date = time.strftime("%m/%d/%Y")

# To grab local ip address


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


local_ip = get_local_ip()


try:
    with open("config.json", "r") as f:
        data = json.load(f)
        # pw = os.getcwd()
        pw = ['C:', 'Users', 'ccarl.Johnson', 'Hercules']
        # pw = pw.split("/")
        name = pw[2]

    if local_ip in data:
        if name in data[local_ip]:
            port = data[local_ip][name]["port"]
        else:
            port = data[local_ip]["*"]["port"]
    else:
        port = data["*"]["port"]

except FileNotFoundError:
    print("Error: File not found.")
    exit()

name = name.split('.')[0]

'''

This class allows us to create http server and get a response from it
BaseHTTPRequestHandler - used to handle the HHTP request that arrive at the server, 
which pre-opens sockets 

'''
class HTTPResponse(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(
            bytes(f"Hello {name.capitalize()}, today is ".encode() + date.encode()))


Server = HTTPServer((local_ip, port), HTTPResponse)
print("IP Address: ", local_ip)
print("Port: ", port)
print("Name: ", name.capitalize())
print("Serever now running")
Server.serve_forever()
Server.server_close()
print("Server stop")
