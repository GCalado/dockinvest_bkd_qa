def get_secret_value(aws_session, secret_name):
    client = aws_session.client("secretsmanager")
    response = client.get_secret_value(SecretId=secret_name)
    assert response.get("SecretString") is not None
    return response.get("SecretString")