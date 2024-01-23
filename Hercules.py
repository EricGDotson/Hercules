# Opening config Java Script Object Notation (json) file
import json
import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

# TODO: put config in gitignore

host = "10.30.25.114"
# port = 1001
date = time.strftime("%m/%d/%Y")
global port
global name
try:
    with open("config.json", "r") as f:
        data = json.load(f)
        pw = os.getcwd()
        pw = pw.split("\\")
        pw = pw.split('.')
        print(pw[2])

    for user in data["users"]:
        if pw[2] == data["users"][0]["name"]:
            port = data["users"][0]["port"]
            name = pw.split('.')

except FileNotFoundError:
    print("Error: File not found.")
    exit()

'''
This class allows us to create http server and get a response from it
BasrHTTPRequestHandler - used to handle the HHTP request that arrive at the server, 
which pre-opens sockets 
'''


class HTTPResponse(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(
            bytes(f"HELLO {name}, today is ".encode() + date.encode()))


Server = HTTPServer((host, port), HTTPResponse)
print("Serever now running")
Server.serve_forever()
Server.server_close()
print("Server stop")

'''
os.walk Append dir to a list
walking through home append names to list then make if statement

if name is in list find that name in json 
grab that name and port number for port and print 


why is config in gitignore
for each name

'''
