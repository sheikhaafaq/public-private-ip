#publicip
from requests import get
def publicIP():
  ip = get('https://api.ipify.org').text
  return ip
