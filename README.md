# dataservice-publisher-etl

## Setup
```
% pyenv virtualenv 3.9.6 dataservice-publisher-etl
% pyenv local dataservice-publisher-etl
% pip install -r requirements.txt
```
.env:
```
DATASERVICE_PUBLISHER_HOST_URL=https://dataservice-publisher.digdir.no
ADMIN_USERNAME=admin
ADMIN_PASSWORD=super_secret
INPUT_FILE=00_input_files/api-catalog_1.json
```
## Run
```
% python 03_load/load.py
```

## Hosts
Test: https://dataservice-publisher.demo.fellesdatakatalog.digdir.no
Prod: https://dataservice-publisher.digdir.no
