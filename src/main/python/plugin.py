from api import *

token = "MzFhYTNiZTAwODg5M2E0NDE3OGUwNWE5ZjYzZWQ2YzllZGFiYWRmNDQwNDBlNmZhZGEzN2I3NTJiOWM2ZWEyZg.aHR0cDovL2xvY2FsaG9zdDo5MDkw"
x = api.ApiClient(token)

print(x.url)
