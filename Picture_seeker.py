import urllib3
import simplejson
import requests
import PIL.Image as Image
import io
import pathlib


manager = urllib3.PoolManager()
searchTerm = input("Input search phrase\n")
# My google API
searchUrl = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDPXV3Nj3vW3B12T4M1YKnCcrghvAFvhsE&cx=3f34f7e4dbe6af60a&q=" + searchTerm + "&searchType=image&fileType=jpg&imgSize=xlarge&alt=json"
r = manager.request('GET', searchUrl)   # Image search
api_output = simplejson.loads(r.data.decode('utf-8'))   # Decode to json format

links = []  # Links to the images

for line in api_output['items']:
    links.append(line['link'])


def download_png(url, path):    # Image saving
    r = requests.get(url)
    img = Image.open(io.BytesIO(r.content))     # Byte string into image
    img.save(path)


path = str(pathlib.Path().absolute()) + "\\Images\\"    # Get current directory and create subdirectory
try:
    pathlib.Path(path).mkdir()
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)


for link in links:
    hashv = str(hash(link))
    new_path = path + hashv + ".png"
    download_png(link, new_path)
