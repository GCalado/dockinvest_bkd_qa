import json
import os
from src.helpers.data_helpers import load_data
from src.helpers.db_helpers import *
from src.helpers.api_helpers import *
from src.helpers.aws_helpers import get_secret_value
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
  db_credentials = dock_invest_db_credentials()
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

def dock_invest_db_credentials():
    dock_invest_db_credentials = {
      "host": os.environ["dock_invest_host"],
      "port": os.environ["dock_invest_port"],
      "dbname": os.environ["dock_invest_dbname"],
      "username": os.environ["dock_invest_username"],
      "password": os.environ["dock_invest_password"]
    }
    return dock_invest_db_credentials