import pytest
import boto3
import json
import os
from dotenv import load_dotenv
from src.helpers.aws_helpers import get_secret_value
from src.helpers.data_helpers import load_data

load_dotenv()

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="hml",
        choices=["dev", "hml"],
        help="Ambiente de execução: dev ou hml (padrão: hml)"
    )


@pytest.fixture(scope="session")
def exec_env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def aws_session(exec_env):
    aws_access_key_id = os.getenv("aws_access_key_id_temp_qa")
    aws_secret_access_key = os.getenv("aws_secret_access_key_temp_qa")
    region_name = os.getenv("region")
    account_id = os.getenv(f"account_{exec_env}")
    role_name = os.getenv("role_name")

    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    sts_client = session.client("sts")
    role_arn = f"arn:aws:iam::{account_id}:role/{role_name}"
    assumed_role = sts_client.assume_role(
        RoleArn=role_arn,
        RoleSessionName="Automation"
    )

    credentials = assumed_role["Credentials"]

    assumed_session = boto3.Session(
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
        region_name=region_name
    )

    urls_secret = json.loads(get_secret_value(assumed_session, "automation_QA_uris"))
    db_secret = json.loads(get_secret_value(assumed_session, "automation_QA_db_access"))
    os.environ.update(urls_secret)
    os.environ.update(db_secret)
    os.environ['ENVIRONMENT'] = exec_env

    return assumed_session