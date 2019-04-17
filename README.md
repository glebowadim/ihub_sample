# ihub_sample
Sample Project for Onevizion Integration Hub

Sample Integration adds integration logs via API and writes message to stdout.

Sample Integration consist of two python files, SimpleIntegration.py and OVIntegration.py.
OVIntegration.py contains methods for working with API. SampleIntegration.py is python script for executing the integration. 

The integration adds logs of the different log levels (Info, Warning, Error, Debug) every 5 seconds. 

PasswordFile.json should be in integration directory. PasswordFile.json contains login, password and url. 

Sample Integration retrieves Process Id from ihub_process_id file for adding logs. ihub_process_id is put into integration directory at each integration run.

If you does not have the possibility to add log via API, then you can use SmallSampleIntegration. SmallSampleIntegration is just a integration with writing to stdout only.

Integration uses print(..., flush = True), so the stdout is synchronized with the Integration Logs. Otherwise, messages from stdout are added after the script is completed.

## Requirements
- Python 3
- Requests - library for python (http://docs.python-requests.org/en/master/)

## Usage
Create new integration with the following fields: 
- Integration Name: Sample Integration
- Command: python3 ./SampleIntegration.py
- Repository: https://github.com/ov-integrations/ihub_sample
- Settings File:  PasswordFile.json

PasswordFile.json

```json
{
"UserName":"amoiseenko",
"Password":"******",
"URL":"http://localhost:8080"
}
```

