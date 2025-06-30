import os
import requests
import json

def get_issuer_history(client_id, product_id, balance_type_config_id = None):
    url = f"{os.environ['dock_invest_issuer_setup_api']}history/{client_id}/{product_id}"
    headers = {
        "x-apigw-api-id": "bvd5t8f4s6",
        "Content-Type": "application/json"
    }
    params = {
        "balanceTypeConfigId": balance_type_config_id,
        "pageSize": 100
    }
    print(f"\nRealizando um GET History \n {url}")
    response = requests.get(url, headers=headers, params=params)
    return response

def post_create_issuer_setup(payload):
    url = f"{os.environ['dock_invest_issuer_setup_api']}"
    headers = {
        "x-apigw-api-id": "bvd5t8f4s6",
        "Content-Type": "application/json"
    }
    print(f"\nRealizando um POST Issuer Setup \n{url} \nCom o payload:")
    print(json.dumps(payload, indent=4))
    response = requests.post(url, headers=headers, json=payload)
    return response

def put_create_issuer_setup(payload, uri_params):
    url = f"{os.environ['dock_invest_issuer_setup_api']}{uri_params['issuerId']}/{uri_params['productId']}/{uri_params['balanceTypeConfigId']}"
    headers = {
        "x-apigw-api-id": "bvd5t8f4s6",
        "Content-Type": "application/json"
    }
    print(f"\nRealizando um PUT Issuer Setup \n{url} \nCom o payload:")
    print(json.dumps(payload, indent=4))
    response = requests.put(url, headers=headers, json=payload)
    return response

def get_issuer_setup(client_id, product_id):
    url = f"{os.environ['dock_invest_issuer_setup_api']}{client_id}?productId={product_id}"
    headers = {
        "x-apigw-api-id": "bvd5t8f4s6",
        "Content-Type": "application/json"
    }
    print(f"\nRealizando um GET Issuer Setup \n{url}")
    response = requests.get(url, headers=headers)
    return response

def delete_issuer_setup(client_id, product_id):
    url = f"{os.environ['dock_invest_issuer_setup_api']}{client_id}/{product_id}"
    headers = {
        "x-apigw-api-id": "bvd5t8f4s6",
        "Content-Type": "application/json"
    }
    print(f"\nRealizando um DELETE Issuer Setup \n{url}")
    response = requests.delete(url, headers=headers)
    return response