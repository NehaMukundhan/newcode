import requests
response = requests.get('http://216.10.245.166/Library/GetBook.php',params={'ID':def2998},)
print(response.text)