import socket

server = socket.socket()

server.bind(("0.0.0.0", 25565))
server.listen()

print("Spark is running!")

player, address = server.accept()

print("Player connected:", address)
