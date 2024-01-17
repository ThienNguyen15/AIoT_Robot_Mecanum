import requests
import time

img_url = 'Link Cam + /capture'
counter = 2000
while True:
    print("Capturing...", counter + 1)
    counter = counter + 1
    response = requests.get(img_url)
    if response.status_code:
        fp = open('Path Store' + str(counter) + '.png', 'wb')
        fp.write(response.content)
        fp.close()
    time.sleep(1)
