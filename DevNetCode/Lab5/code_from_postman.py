import requests

url = "https://198.18.129.100/api/v1/ticket"

payload = " {\r\n \"username\" : \"admin\",\r\n \"password\" : \"C1sco12345\"\r\n }"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "5f62f80f-7efd-b1ff-b1f4-24838f6c2f31"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)