import OVIntegration
import json
import time

with open('settings.json', "rb") as SFile:
    passwordData = json.loads(SFile.read().decode('utf-8'))

user = passwordData["UserName"]
password = passwordData["Password"]
site = passwordData["URL"]

with open('ihub_parameters.json', "rb") as PFile:
    ihub_data = json.loads(PFile.read().decode('utf-8'))

processId = ihub_data['processId']

i = 0
while i < 3:
    time.sleep(5)
    integrationOV = OVIntegration.OVIntegration(processId=processId, url=site, userName=user, password=password)
    i = i + 1
    print(i, flush = True)
