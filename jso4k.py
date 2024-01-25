import json


def write_to_file(user_data):
    json_string = json.dumps(user_data, ensure_ascii=False)
    print(json_string)
    with open('./db.json', 'w', encoding='utf-8') as file:
        file.write(json_string)
    print('готово')

def read_from_db():
    try:
        with open('./db.json', encoding='utf-8') as file:
            json_string = file.readline()
        db_data = json.loads(json_string)
    except FileNotFoundError:
        db_data = {}
    print(db_data)
    return db_data

