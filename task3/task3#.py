import json


with open('tests.json', 'r') as f:
    tests_data = json.load(f)


with open('values.json', 'r') as f:
    values_data = json.load(f)


for test_item in tests_data:
    if 'values' in test_item:

        for value_item in test_item['values']:
            if 'id' in value_item:
                for value_data in values_data:
                    if 'id' in value_data and value_data['id'] == value_item['id']:
                 
                        value_item['value'] = value_data.get('value', '')


with open('report.json', 'w') as f:
    json.dump(tests_data, f, indent=4)
