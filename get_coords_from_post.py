import requests

url = "https://ghanapostgps.sperixlabs.org/get-location"

payload = 'address=AK-448-5038'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

# print(response.json())

data = response.json()['data']['Table'][0]

# Print key, value pairs
for key in data.keys():
    print(f'{key}: {data[key]}')
