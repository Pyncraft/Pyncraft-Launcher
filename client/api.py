import requests
from conf import server

def isOnline():
    r = requests.get(f"{server}/api/up")
    if r.status_code == 200:
        return True
    elif r.status_code == 500:
        return False
def versions():
    r = requests.get(f"{server}/api"/versions)