# dataservice-publisher-etl

## Setup
```
% pyenv virtualenv 3.8.6 dataservice-publisher-etl
% pyenv local dataservice-publisher-etl
% pip install -r requirements.txt
```
.env:
```
DATASERVICE_PUBLISHER_HOST_URL=https://dataservice-publisher.digdir.no
ADMIN_USERNAME=admin
ADMIN_PASSWORD=super_secret
```
## Run
```
% python 03_load/load.py
```
