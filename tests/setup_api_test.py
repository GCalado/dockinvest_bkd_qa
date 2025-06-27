import pytest
import uuid
from src.mocks.create_issuer_setup_mock import create_issuer_setup_payload
from src.helpers.common_helpers import *
from src.helpers.api_helpers import *

def test_validate_same_history_size_in_database_and_api():
    client_id = load_data(['dock_one_data', 'client_id'])
    product_id = load_data(['dock_one_data', 'product_id'])
    total_api_history_size = get_total_history_size(client_id, product_id)
    print("O total de registros na API de histórico é:", total_api_history_size)

    total_db_history_size = get_issuer_history_total(client_id, product_id)

    assert total_db_history_size == total_api_history_size

@pytest.mark.parametrize(
    "key, value, expected_status, expected_contract",
    [
        pytest.param("issuerId", "test", 422, "undetailed_error", id="issuerId_string"),
        pytest.param("issuerId", f"{uuid.uuid4()}", 404, "undetailed_error", id="issuerId_random_uuid"),
        pytest.param("issuerId", "", 422, "undetailed_error", id="issuerId_empty_string"),
        pytest.param("issuerId", None, 422, "detailed_error", id="issuerId_null"),
        pytest.param("issuerId", False, 422, "detailed_error", id="issuerId_boolean"),
        pytest.param("issuerId", 103, 422, "detailed_error", id="issuerId_number"),
        pytest.param("productId", "test", 422, "undetailed_error", id="productId_string"),
        pytest.param("productId", f"{uuid.uuid4()}", 404, "undetailed_error", id="productId_random_uuid"),
        pytest.param("productId", None, 422, "detailed_error", id="productId_null"),
        pytest.param("productId", False, 422, "detailed_error", id="productId_boolean"),
        pytest.param("productId", 103, 422, "detailed_error", id="productId_number"),
        pytest.param("balanceTypeConfigId", None, 422, "detailed_error", id="balanceTypeConfigId_null"),
        pytest.param("balanceTypeConfigId", False, 422, "detailed_error", id="balanceTypeConfigId_boolean"),
        pytest.param("balanceTypeConfigId", 103, 422, "detailed_error", id="balanceTypeConfigId_number"),
        pytest.param("operationStepConfigId", "test", 404, "undetailed_error", id="operationStepConfigId_string"),
        pytest.param("operationStepConfigId", f"{uuid.uuid4()}", 404, "undetailed_error", id="operationStepConfigId_random_uuid"),
        pytest.param("operationStepConfigId", "", 404, "undetailed_error", id="operationStepConfigId_empty_string"),
        pytest.param("operationStepConfigId", None, 422, "detailed_error", id="operationStepConfigId_null"),
        pytest.param("operationStepConfigId", False, 422, "detailed_error", id="operationStepConfigId_boolean"),
        pytest.param("operationStepConfigId", 103, 422, "detailed_error", id="operationStepConfigId_number"),
        pytest.param("configOperationStepId", "test", 422, "undetailed_error", id="configOperationStepId_string"),
        pytest.param("configOperationStepId", f"{uuid.uuid4()}", 404, "undetailed_error", id="configOperationStepId_random_uuid"),
        pytest.param("configOperationStepId", None, 422, "detailed_error", id="configOperationStepId_null"),
        pytest.param("configOperationStepId", False, 422, "detailed_error", id="configOperationStepId_boolean"),
        pytest.param("configOperationStepId", 103, 422, "detailed_error", id="configOperationStepId_number"),
        pytest.param("splitPercentage", "test", 422, "detailed_error", id="splitPercentage_string"),
        pytest.param("splitPercentage", 101, 422, "detailed_error", id="splitPercentage_higher_than_100"),
        pytest.param("splitPercentage", -1, 422, "detailed_error", id="splitPercentage_lower_than_0"),
        pytest.param("splitPercentage", None, 422, "detailed_error", id="splitPercentage_null"),
        pytest.param("remunerationPercentage", "test", 422, "detailed_error", id="remunerationPercentage_string"),
        pytest.param("remunerationPercentage", 201, 422, "detailed_error", id="remunerationPercentage_higher_than_200"),
        pytest.param("remunerationPercentage", -1, 422, "detailed_error", id="remunerationPercentage_lower_than_0"),
        pytest.param("remunerationPercentage", None, 422, "detailed_error", id="remunerationPercentage_null"),
        pytest.param("cuttingTime", True, 422, "detailed_error", id="cuttingTime_boolean"),
        pytest.param("cuttingTime", 135, 422, "detailed_error", id="cuttingTime_number"),
        pytest.param("cuttingTime", None, 422, "detailed_error", id="cuttingTime_null"),
        pytest.param("remunerationDay", "QA_Test", 422, "detailed_error", id="remunerationDay_not_enum"),
        pytest.param("remunerationDay", None, 422, "detailed_error", id="remunerationDay_null"),
        pytest.param("issuerDestinationAccount", 135, 422, "detailed_error", id="issuerDestinationAccount_number"),
        pytest.param("issuerDestinationAccount", None, 422, "detailed_error", id="issuerDestinationAccount_null"),
        pytest.param("issuerDestinationAccount", True, 422, "detailed_error", id="issuerDestinationAccount_false"),
        pytest.param("minimumInvestmentBalance", -1, 422, "detailed_error", id="minimumInvestmentBalance_lower_than_0"),
        pytest.param("minimumInvestmentBalance", "QA_Test", 422, "detailed_error", id="minimumInvestmentBalance_number"),
        pytest.param("minimumInvestmentBalance", None, 422, "detailed_error", id="minimumInvestmentBalance_null"),
        pytest.param("baseRemunerationIndex", "QA_Test", 422, "detailed_error", id="baseRemunerationIndex_not_enum"),
        pytest.param("baseRemunerationIndex", None, 422, "detailed_error", id="baseRemunerationIndex_null"),
        pytest.param("paymentFrequency", "QA_Test", 422, "detailed_error", id="paymentFrequency_not_enum"),
        pytest.param("paymentFrequency", None, 422, "detailed_error", id="paymentFrequency_null"),
        pytest.param("calendarId", False, 422, "detailed_error", id="calendarId_boolean"),
        pytest.param("calendarId", 115, 422, "detailed_error", id="calendarId_number"),
        pytest.param("calendarId", None, 422, "detailed_error", id="calendarId_null"),
        pytest.param("issuerAccountBonification", False, 422, "detailed_error", id="issuerAccountBonification_boolean"),
        pytest.param("issuerAccountBonification", 103, 422, "detailed_error", id="issuerAccountBonification_boolean"),
        pytest.param("issuerAccountBonification", None, 422, "detailed_error", id="issuerAccountBonification_null"),
    ]
)
def test_validate_negative_scenarios_post(key, value, expected_status, expected_contract):
    payload = create_issuer_setup_payload()
    payload[key] = value
    response = post_create_issuer_setup(payload)
    response_body = response.json()
    print(response.status_code)
    assert response.status_code == expected_status
    print(f"ResponseBody: \n{json.dumps(response_body, indent=4)}")
    validate_contract(response_body, expected_contract)

def test_validate_error_issuer_already_exists():
    issuer_payload = select_one_valid_issuer_setup()
    print(f"aaaaaaaaaaaaaaaaaaa\n{issuer_payload[0]}")