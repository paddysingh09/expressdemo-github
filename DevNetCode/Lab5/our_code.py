#Import necessary modules
import requests
import json

#Disable warnings
requests.packages.urllib3.disable_warnings()

# Variables
apic_em_ip = "https://198.18.129.100/api/v1"
api_call ="/ticket"

#Payload contains authentication information
payload = {"username":"admin","password":"C1sco12345"}

# Header information
headers = {"content-type" : "application/json"}

# Combine apic_em_ip and api_call variables into one variable call url
url = apic_em_ip + api_call

response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

# Print the respond body
print(response.text)