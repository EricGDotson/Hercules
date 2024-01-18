#Pseudocode

Refernces: 
    https://docs.python.org/3/library/socket.html
    https://docs.python.org/3/howto/sockets.html
    https://thepythoncode.com/assistant/transformation-details/python-script-listening-to-a-specific-port/#google_vignette


http://google.com:80
https://google.com:443
https://google.com:47524

http://192.168.10.100:1001 # eric
http://192.168.10.100:1002 # nate
http://192.168.10.100:1003 # josht
http://192.168.10.100:1004 # evan
http://192.168.10.100:1005 # tom


Github:
    .gitignore *config.json

JOAN:
    /home/eric.dotson/Hercules/.hercules.config.json   ($name = 'Eric', $port = 1001)
    /home/nate.klauer/Hercules/.hercules.config.json   ($name = 'Nate', $port = 1002)
    /home/tom.wise/Hercules/.hercules.config.json      ($name = 'Tom', $port = 1005)



CODE:

    Open config file (.hecules.config.json)
    Parse config file #https://www.w3schools.com/python/python_json.asp
    If fail exit

    Bind to {port}
    If fail exit

    Give HTTP response of "Hello {name} today is {day}"


exit




#NOTE:
''''
Socket - Low level networking interface

'''