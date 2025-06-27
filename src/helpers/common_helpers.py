import json
import os
import pytest
from src.helpers.data_helpers import *
from src.helpers.db_helpers import *
from src.helpers.api_helpers import *
from src.mocks.create_issuer_setup_mock import create_issuer_setup_payload
from src.helpers.aws_helpers import get_secret_value
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from datetime import date, timedelta

def get_previous_business_day(start_date):
  last_day = start_date - timedelta(days=1)
  while last_day.weekday() >= 5:  # 5 = sábado, 6 = domingo
      last_day -= timedelta(days=1)
  return last_day

def get_last_business_day_balances(aws_session):
  secret = get_secret_value(aws_session, load_data(["secrets_manager", "dock_invest_db"]))
  db_credentials = json.loads(secret)
  total_balance = get_total_balance(dock_invest_db_credentials())
  return total_balance

def get_total_balance(db_credentials):
  operation = "SELECT SUM(current_balance) FROM"
  table_name = "dock_invest.daily_balance"
  condition = "WHERE account_status = 'ACTIVE' AND balance_has_been_used = TRUE AND balance_date >"
  last_business_day =  "CURRENT_DATE - INTERVAL '5 DAYS'"
  # last_business_day =  get_previous_business_day(date.today()).strftime("'%Y-%m-%d'")
  query = f"{operation} {table_name} {condition} {last_business_day}"
  print(f"Executing query: {query}")
  result = run_postgres_select(db_credentials, query)
  assert result is not None
  return result[0]

def get_issuer_history_total(client_id, product_id, balance_type_config_id=None):
  balance_type_config_id = "1234" if balance_type_config_id is None else balance_type_config_id
  db_credentials = set_database_credentials("dock_invest")
  operation = "SELECT COUNT(*) FROM"
  table_name = "dock_invest.issuer_history"
  condition = f"WHERE issuer_id = '{client_id}' and product_id = '{product_id}' and balance_type_config_id = '{balance_type_config_id}'"
  query = f"{operation} {table_name} {condition}"
  print(f"Executing query: {query}")
  result = run_postgres_select(db_credentials, query)
  print(f"Quantidade de registros no banco é {result[0][0]}")
  assert result is not None
  return result[0][0]

def get_total_history_size(client_id, product_id, balance_type_config_id=None):
    balance_type_config_id = "1234" if balance_type_config_id is None else balance_type_config_id
    issuer_history = get_issuer_history(client_id, product_id, balance_type_config_id)
    return len(issuer_history['results'])

def validate_contract(response_body, expected_contract):
    schema = load_contract(f"{expected_contract}.json")
    try:
        validate(instance=response_body, schema=schema)
    except ValidationError as e:
        pytest.fail(f"Resposta não bate com o schema '{expected_contract}': {e.message}")

def select_one_valid_issuer_setup():
  db_credentials = set_database_credentials("dock_invest")
  operation = "SELECT row_to_json(t) FROM (SELECT * FROM"
  table_name = "dock_invest.issuer"
  condition = f"WHERE is_active = True) t"
  query = f"{operation} {table_name} {condition}"
  print(f"Executing query: {query}")
  result = run_postgres_select(db_credentials, query)
  return result[0][0]

def validate_error_duplicated_issuer_setup(issuer_setup_infos):
    issuer_setup_payload = create_issuer_setup_payload()
    issuer_setup_payload["issuerId"] = issuer_setup_infos["issuer_id_pk"]
    issuer_setup_payload["productId"] = issuer_setup_infos["product_id_pk"]
    issuer_setup_payload["balanceTypeConfigId"] = issuer_setup_infos["balance_type_config_id_pk"]
    response = post_create_issuer_setup(issuer_setup_payload)
    assert response.status_code == 409, f"Expected status code 409, got {response.status_code}"
    response_body = response.json()
    print(f"ResponseBody: \n{json.dumps(response_body, indent=4)}")
    validate_contract(response_body, "undetailed_error")
    assert response_body['title'] == "Issuer already exists"
    assert response_body['message'] == "Issuer ID already exists"