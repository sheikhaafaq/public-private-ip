#private ip
import socket
def privateIP():
  hostname = socket.gethostname()
  local_ip = socket.gethostbyname(hostname)
  return local_ip

print(privateIP())
