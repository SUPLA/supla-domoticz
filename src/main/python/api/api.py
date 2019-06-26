import base64


class ApiClient:
    def __init__(self, token):
        self.token = token
        split = token.split(".")
        self.url = base64.b64decode(split[1]).decode('UTF-8')

    def find_all_devices(self):
        pass

    def find_device(self, device_id):
        pass


class Device:
    def __init__(self, name):
        self.name = name
