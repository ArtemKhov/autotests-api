import json

json_data = '{"name": "Иван", "age": 24, "city": "New York"}'
parser_data = json.loads(json_data)
print(parser_data)

data = {"name": "Ольга", "age": 33, "city": "Спб"}
json_strings = json.dumps(data, indent=4, ensure_ascii=False)
print(json_strings)


with open("json_example.json", "r", encoding='utf-8') as file:
    read_data = json.load(file)
    print(read_data)


with open("json_user.json", "w", encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)