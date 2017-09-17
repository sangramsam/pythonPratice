import random
import urllib.request

def download_web_image(url):
    name=random.randrange(1,2000)
    full_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)


download_web_image('http://opinio.workzie.com/api/docs/getExpenseFile/1fcb04a3-9959-41d4-a698-53c29ebdc4ce.jpeg')