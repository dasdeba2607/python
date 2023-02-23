def process_json(data, level):
    if isinstance(data, dict):
        for key, value in data.items():
            process_json(value, level + 1)
    elif isinstance(data, list):
        for item in data:
            process_json(item, level)
    else:
        print("Level", level, "Value:", data)


# sample JSON data
json_data = '''
{
    "firstName": "John",
    "lastName": "Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94122"
    }
}'''

process_json(json_data,0)
