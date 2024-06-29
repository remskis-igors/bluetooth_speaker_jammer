# device.py

class Device:
    def __init__(self, address, name=None):
        self.address = address
        self.name = name

    def __str__(self):
        return f"Device(address={self.address}, name={self.name})"
