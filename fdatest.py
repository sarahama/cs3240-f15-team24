import requests
import urllib.request
from Crypto.Cipher import AES

def decrypt_file(in_filename, key):
    out_filename = "DEC_" + in_filename
    aes = AES.new(key)
    with open(in_filename, 'rb') as in_file:
        with open(out_filename, 'wb') as out_file:
            while True:
                chunk = in_file.read(1024)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                out_file.write(aes.decrypt(chunk))

username = input("Username: ")
password = input("Password: ")
info = {'username': username, 'password':password}
r = requests.get("http://127.0.0.1:8000/communicate/", params=info)
response = r.json()
if not response['valid']:
    print("Invalid username and password")
elif response['valid']:
    print("Welcome ", response['username'] + "!\n")
    reports = response['reports']
    #display this user's reports
    print("Your reports:\n")
    for entry in reports:
        print(entry)

    key = input("\nEnter the key of the report you would like to view: ")
    info2 = {'key':key}
    r2 = requests.get("http://127.0.0.1:8000/communicate2/", params=info2)
    response2 = r2.json()
    print()
    print("Title: ", response2['report_title'])
    print("Owner: ", response2['report_owner'])
    print("Short Description: ", response2['report_short_description'])
    print("Long Description: ", response2['report_long_description'])
    print("Date: ", response2['report_creation_date'])
    print("Public: ", response2['report_public'])
    print("Files: ")
    for file in response2['files']:
        print("\t", file)

    filekey = input("\nEnter the key of the file you would like to view: ")
    info3 = {'filekey':filekey}
    r3 = requests.get("http://127.0.0.1:8000/communicate3/", params=info3)
    response3 = r3.json()
    url = "http://127.0.0.1:8000" + response3['url']
    file_name = url.split("/")[-1]
    urllib.request.urlretrieve(url, file_name)
    if response3['encrypted']:
        privatekey = input("Enter the private key to decrypt the file: ")
        decrypt_file(file_name, privatekey)