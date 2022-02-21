import subprocess
import sys

# install dependencies of integration
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'python_dependencies.txt'])

from sample import Integration
import json
from jsonschema import validate
from onevizion import IntegrationLog

# read, parse, and validate integration settings file
with open('settings_schema.json', "rb") as PFile:
    json_schema = json.loads(PFile.read().decode('utf-8'))

with open('settings.json', "rb") as SFile:
    settings_file_json = json.loads(SFile.read().decode('utf-8'))

try:
    validate(instance=settings_file_json, schema=json_schema)
except Exception as e:
    raise Exception("Incorrect value in the settings file\n {}".format(str(e))) from e

access_key = settings_file_json["OneVizionAccessKey"]
secret_key = settings_file_json["OneVizionSecretKey"]
url = settings_file_json["OneVizionURL"]

# read standard integration environment properties
with open('ihub_parameters.json', "rb") as PFile:
    ihub_data = json.loads(PFile.read().decode('utf-8'))

process_id = ihub_data['processId']  # Process ID of the current Integration Run in OneVizion
log_level = ihub_data['logLevel']  # Log Level retrieved from settings of the Integration in OneVizion

# initialize logging
integration_log = IntegrationLog(URL=url.replace("https://", "").replace("http://", ""),
                                 userName=access_key,
                                 password=secret_key,
                                 isTokenAuth=True,
                                 processId=process_id,
                                 logLevelName=log_level)

integration = Integration(integration_log)
# start the main integration code
integration.start()
