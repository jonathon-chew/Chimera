def download_Image(URL, fileName):
    import time
    import random
    import requests
    with requests.get(URL, stream=True) as r:
        r.raise_for_status()
        with open (fileName, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    sleepTime = random.randrange(1,4)
    print(f"I'm sleeping for {sleepTime}")
    time.sleep(sleepTime)
