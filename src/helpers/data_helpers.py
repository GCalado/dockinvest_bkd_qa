import yaml
import os
import json
from pathlib import Path

def load_yaml_data(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def search_data(keys, data):
    for key in keys:
        if data is None:
            break
        data = data.get(key)
    return data

def load_data(keys):
    data = load_yaml_data(f"tests/data/{os.environ['env']}.yaml")
    if data is None:
        data = load_yaml_data("tests/data/standard.yaml")
    result = search_data(keys, data)
    return result

def load_contract(contract_name):
    contract_path = Path(__file__).parent.parent / f"schemas/{contract_name}"
    with open(contract_path, 'r') as file:
        return json.load(file)