import json

json_data_source = 'data.json'

with open(json_data_source, encoding='utf-8') as data:
    anomalies = json.load(data)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), int(value)
    print(f'{year} ...{value:6.2f}')