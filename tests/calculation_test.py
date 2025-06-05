from src.helpers.common_helpers import *

def test_validate_last_day_gross_calculation(aws_session):
    last_business_day_balances = get_last_business_day_balances(aws_session)
    print(last_business_day_balances)
    
