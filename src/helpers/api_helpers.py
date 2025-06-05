import os
import requests

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
    print(response.status_code)
    assert response.status_code == 200
    return response.json()
    