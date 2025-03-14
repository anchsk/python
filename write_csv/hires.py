""" 
users_in.csv
username,password,real_name

amanda,,Amanda Alonso
ian,,Ian Ortega
eugene,,Eugene Konya
[...]

0. read a list
1. generate random passwords
2. create their accounts (linux)
3. write passwords back to a new CSV file
"""

import csv
import secrets
import subprocess
from pathlib import Path # to locate the data files

cwd = Path.cwd()/'write_csv'
print(cwd)
with open(cwd/"data/users_in.csv", "r") as file_input, open(cwd/"data/users_out.csv", "w") as file_output:
    reader = csv.DictReader(file_input)
    writer = csv.DictWriter(file_output, fieldnames=reader.fieldnames)
    writer.writeheader()
    
    for user in reader:
        # print(user)
        """ {'username': 'oliver', 'password': '', 'real_name': 'Oliver Garcia'} """
        user["password"] = secrets.token_hex(8)
       # This is for linux:
       # useradd_cmd = ["/sbin/useradd", 
       #               "-c", user["real_name"], 
       #               "-m", 
       #               "-G", "users", 
       #               "-p", user["password"], 
       #               user["username"]]
       # subprocess.run(useradd_cmd, check=True)
        writer.writerow(user)
        
        

