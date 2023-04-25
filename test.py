import requests as re
import threading



def hi():
    
    re.post('https://webhook.site/9ebe462f-59a3-4da9-a054-f7c2acb3f8b8')

threads = []

for i in range(2):
    t = threading.Thread(target=hi)
    t.daemon = True
    threads.append(t)

for i in range(2):
        threads[i].start()

for i in range(2):
        threads[i].join()