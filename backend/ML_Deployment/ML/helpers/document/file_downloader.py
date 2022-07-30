from django.utils.crypto import get_random_string
import os,sys
import requests

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)

from paths import TEMP_DIR

def downloader(url):
    file_name = get_random_string(length=32)+'.pdf'
    file_path = os.path.join(TEMP_DIR,file_name)

    r = requests.get(url)

    with open(file_path,'wb') as f:
        f.write(r.content)
    return file_path
