# import sys
# urllib (standard library)

import urllib.request
from pathlib import Path
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = f'{Path(__file__).parent}/Example1.txt'
urllib.request.urlretrieve(url, filename)
# print(Path.cwd())
# print(Path(__file__).parent)
## Download Example file
# wget Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt


# sys.exit()
# requests library
import requests 

# downloads entire file into memory
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
response = requests.get(url)
if response.status_code == 200:
    with open('download_file/Example2.txt', 'wb') as file: 
        # initialize file variable here ^ as file
        file.write(response.content)
    print("Downloaded successfully!")
else:
    print('Failed. Status code: {}'.format(response.status_code))

print(file.name, file.mode)
# Example2.txt, r

file = open('download_file/Example2.txt', 'r')
content = file.read()
print(content) 
file.close()

# a better way to open a file
with open('download_file/Example2.txt', 'r') as file1:
    # content = file1.read()
    # print(content)
    # print(file1.readline())
    # print(file1.readline(5))
    list1 = file1.readlines()
    print(list1, 'list')

print(list1[0]) # This is line 1 \n
    
print(file1.closed) # verify that the file is closed
