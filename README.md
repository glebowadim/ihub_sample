# ihub_sample
Sample Project for Onevizion Integration Hub

Sample Integration adds integration logs via API and writes messages to stdout.

Sample Integration consists of two python files, SimpleIntegration.py and OVIntegration.py.
ovintegration.py contains a class for working with API. SampleIntegration.py is executable python script. 

The integration adds logs of the different log levels (Info, Warning, Error, Debug) every 5 seconds. 

settings.json should be in integration directory. settings.json contains login, password and url. 

Sample Integration retrieves Process Id from ihub_process_id file for adding logs. ihub_process_id is put into integration directory at each integration run.

If you don't have the possibility to add the log via API, then you can use SmallSampleIntegration. SmallSampleIntegration is just a integration with writing to stdout only.

Integration uses print(..., flush=True), so the stdout is synchronized with the Integration Logs. Otherwise, messages from stdout are added after the script is completed.

## Requirements
- Python 3
- Requests, library for python (http://docs.python-requests.org/en/master/)
- onevizion library
- jsonschema library

## Usage
Create a new integration with the following fields: 
- Integration Name: Sample Integration
- Command: python3 ./SampleIntegration.py
- Repository: https://github.com/ov-integrations/ihub_sample
- Settings File: settings.json


settings.json

```json
{
"UserName":"amoiseenko",
"Password":"******",
"URL":"http://localhost:8080"
}
```

