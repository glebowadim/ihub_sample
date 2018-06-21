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
integration = PasswordData["Integration"]

i = 0
while i < 3:
    time.sleep(5)
    integrationOV = OVIntegration.OVIntegration(integrationName=integration, url=site, userName=user, password=password)
    i = i + 1
    print(i)
