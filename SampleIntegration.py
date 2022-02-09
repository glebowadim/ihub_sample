import time
import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'python_dependencies.txt'])

import json
from jsonschema import validate
from ovintegration import OVIntegration

with open('settings_schema.json', "rb") as PFile:
    json_schema = json.loads(PFile.read().decode('utf-8'))

with open('settings.json', "rb") as SFile:
    settings_file_json = json.loads(SFile.read().decode('utf-8'))

try:
    validate(instance=settings_file_json, schema=json_schema)
except Exception as e:
    raise Exception("Incorrect value in the settings file\n {}".format(str(e))) from e

user = settings_file_json["UserName"]
password = settings_file_json["Password"]
url = settings_file_json["URL"]

with open('ihub_parameters.json', "rb") as PFile:
    ihub_data = json.loads(PFile.read().decode('utf-8'))

process_id = ihub_data['processId']
log_level = ihub_data['logLevel']

ov_integration = OVIntegration(process_id=process_id,
                               url=url,
                               user_name=user,
                               password=password,
                               log_level_name=log_level)

for i in range(3):
    time.sleep(5)
    ov_integration.add_log()
    print(i, flush=True)
