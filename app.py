import requests
import time
test = "COde Smell Testing"
x = 150

def githubStatus():
    url = "https://github.com/"
    response = requests.get(url)
    time.sleep(120)
    if response.status_code == 200:
        print("Git Hub is reachable")
    else:
        print(f"Git hub is not reachable with status code : {response.status_code}")

#Calling the function
githubStatus()
