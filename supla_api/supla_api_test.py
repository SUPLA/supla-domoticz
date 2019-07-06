from supla_api import *


def test_token():
    token = "MzFhYTNiZTAwODg5M2E0NDE3OGUwNWE5ZjYzZWQ2YzllZGFiYWRmNDQwNDBlNmZhZGEzN2I3NTJiOWM2ZWEyZg" \
            ".aHR0cDovL2xvY2FsaG9zdDo5MDkw"
    api_client = supla_api.ApiClient(token, lambda msg: print(msg), lambda msg: print(msg))
    assert api_client.token == token


def test_url():
    token = "MzFhYTNiZTAwODg5M2E0NDE3OGUwNWE5ZjYzZWQ2YzllZGFiYWRmNDQwNDBlNmZhZGEzN2I3NTJiOWM2ZWEyZg" \
            ".aHR0cDovL2xvY2FsaG9zdDo5MDkw"
    api_client = supla_api.ApiClient(token, lambda msg: print(msg), lambda msg: print(msg))
    assert api_client.url == "http://localhost:9090"
