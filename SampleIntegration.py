import OVIntegration
import json
import time

with open('settings.json', "rb") as PFile:
    passwordData = json.loads(PFile.read().decode('utf-8'))

user = passwordData["UserName"]
password = passwordData["Password"]
site = passwordData["URL"]

with open('ihub_process_id', "rb") as PFile:
    processId = PFile.read().decode('utf-8')

i = 0
while i < 3:
    time.sleep(5)
    integrationOV = OVIntegration.OVIntegration(processId=processId, url=site, userName=user, password=password)
    i = i + 1
    print(i, flush = True)
