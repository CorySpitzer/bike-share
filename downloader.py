# Download all the files from https://divvy-tripdata.s3.amazonaws.com/index.html
# print("Hello")

# Modified from https://likegeeks.com/downloading-files-using-python/
import requests

# Test the file downloading
base_url = 'https://divvy-tripdata.s3.amazonaws.com/'
test_url = 'https://divvy-tripdata.s3.amazonaws.com/202004-divvy-tripdata.zip'
test_file = requests.get(test_url)
# local_path = '/home/cory/wsl-side-code/data/bike-share/202004-divvy-tripdata.zip'
# open(local_path, 'wb').write(test_file.content)

# note: 37 up to name change
# First 8 download loop:
for i in range(4, 13): #not including 13
    url = base_url + '2020' + str(i).zfill(2) + '-divvy-tripdata.zip'
    data_file = requests.get(url)
    local_path = '/home/cory/wsl-side-code/data/bike-share/bike-data/2020' + str(i).zfill(2) + '-divvy-tripdata.zip' 
    open(local_path, 'wb').write(data_file.content)
    print("Downloaded file " + local_path)

print('finished 2020 batch!')

for j in range(1, 3):
    for i in range(1, 13):
        url = base_url + '202' + str(j) + str(i).zfill(2) + '-divvy-tripdata.zip'
        data_file = requests.get(url)
        local_path = '/home/cory/wsl-side-code/data/bike-share/bike-data/202' + str(j) + str(i).zfill(2) + '-divvy-tripdata.zip' 
        open(local_path, 'wb').write(data_file.content)
        print("Downloaded file " + local_path)

print('finished 2021/22 batch!')


# From https://stackoverflow.com/questions/45540860/download-all-the-files-in-the-website
# from bs4 import BeautifulSoup

# import requests
# r  = requests.get("https://divvy-tripdata.s3.amazonaws.com/index.html")
# data = r.text
# soup = BeautifulSoup(data)

# for link in soup.find_all('a'):
#     print(link.get('href'))

import bs4
import requests

url = "https://divvy-tripdata.s3.amazonaws.com/index.html"
r = requests.get(url)
data = bs4.BeautifulSoup(r.text, "html.parser")
for l in data.find_all("a"):
    r = requests.get(url + l["href"])
    print(r.status_code)

