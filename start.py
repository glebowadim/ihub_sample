import subprocess
import sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'python_dependencies.txt'])

from sample import Integration
import json
from jsonschema import validate

with open('settings_schema.json', "rb") as PFile:
    json_schema = json.loads(PFile.read().decode('utf-8'))

with open('settings.json', "rb") as SFile:
    settings_file_json = json.loads(SFile.read().decode('utf-8'))

try:
    validate(instance=settings_file_json, schema=json_schema)
except Exception as e:
    raise Exception("Incorrect value in the settings file\n {}".format(str(e))) from e

user = settings_file_json["OneVizionUser"]
password = settings_file_json["OneVizionSecurityToken"]
url = settings_file_json["OneVizionURL"]

with open('ihub_parameters.json', "rb") as PFile:
    ihub_data = json.loads(PFile.read().decode('utf-8'))

process_id = ihub_data['processId']
log_level = ihub_data['logLevel']

integration = Integration(url=url,
                          user_name=user,
                          password=password,
                          process_id=process_id,
                          log_level_name=log_level)

integration.start()
