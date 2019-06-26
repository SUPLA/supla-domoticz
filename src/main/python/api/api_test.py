import unittest
from api import *


class ApiTest(unittest.TestCase):
    def test_token(self):
        token = "MzFhYTNiZTAwODg5M2E0NDE3OGUwNWE5ZjYzZWQ2YzllZGFiYWRmNDQwNDBlNmZhZGEzN2I3NTJiOWM2ZWEyZg.aHR0cDovL2xvY2FsaG9zdDo5MDkw"
        api_client = ApiClient(token)
        self.assertEqual(api_client.token, token)

    def test_url(self):
        token = "MzFhYTNiZTAwODg5M2E0NDE3OGUwNWE5ZjYzZWQ2YzllZGFiYWRmNDQwNDBlNmZhZGEzN2I3NTJiOWM2ZWEyZg.aHR0cDovL2xvY2FsaG9zdDo5MDkw"
        api_client = ApiClient(token)
        self.assertEqual(api_client.url, "http://localhost:9090")
