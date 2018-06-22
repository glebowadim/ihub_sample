import OVIntegration
import json
import os
import time

print(os.path.exists('PasswordFile.json'))
with open('PasswordFile.json', "rb") as PFile:
    PasswordData = json.loads(PFile.read().decode('utf-8'))

user = PasswordData["UserName"]
password = PasswordData["Password"]
site = PasswordData["URL"]

print(os.path.exists('Params.json'))
with open('Params.json', "rb") as PFile:
    ParamsData = json.loads(PFile.read().decode('utf-8'))

processId = ParamsData["Process_id"]

i = 0
while i < 3:
    time.sleep(5)
    integrationOV = OVIntegration.OVIntegration(processId=processId, url=site, userName=user, password=password)
    i = i + 1
    print(i)
