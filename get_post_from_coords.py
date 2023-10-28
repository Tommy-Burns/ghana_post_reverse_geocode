import requests

url = "https://ghanapostgps.sperixlabs.org/get-address"

payload = {'lat': '6.742206999587509', 'long': '-1.503308013667684'}
files = []
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

data = response.json()['data']['Table'][0]

# Print key, value pairs
for key in data.keys():
    print(f'{key}: {data[key]}')
