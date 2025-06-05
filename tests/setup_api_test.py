from src.helpers.common_helpers import *
from src.helpers.api_helpers import *

def test_validate_same_history_size_in_database_and_api(aws_session):
    client_id = load_data(['dock_one_data', 'client_id'])
    product_id = load_data(['dock_one_data', 'product_id'])
    total_api_history_size = get_total_history_size(client_id, product_id)
    print("O total de registros na API de histórico é:", total_api_history_size)

    total_db_history_size = get_issuer_history_total(aws_session, client_id, product_id)

    assert total_db_history_size == total_api_history_size