import sys
import requests



print(sys.version)
print(sys.executable)

def greet(who):
  greeting ="Hello, {}".format(who)
  return greeting



r = requests.get("https://coreyms.com")
print(r.status_code)

print("hallo")