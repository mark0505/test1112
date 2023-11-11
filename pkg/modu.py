# pkg/modu.py

import json

def read_json(file_name: str) -> dict:
    """
    將 json 檔案轉為字典後回傳
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def print_json(data: dict) -> None:
    """
    將字典轉為 json 字串後輸出到螢幕
    """
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    print(json_str)

def process_data(data: dict, discount: float) -> None:
    """
    將字典中每個菜品的價格打 discount 折數
    """
    for category in data['categories']:
        for item in category['items']:
            item['price'] *= discount

def write_json(data: dict, file_name: str) -> None:
    """
    將字典轉為檔案
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
