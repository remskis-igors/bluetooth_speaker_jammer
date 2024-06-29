# scanner.py

from bluepy.btle import Scanner, DefaultDelegate

class BluetoothScanner:
    def __init__(self):
        self.scanner = Scanner().withDelegate(MyDelegate())

    def scan_devices(self, scan_time=10):
        devices = self.scanner.scan(scan_time)
        return devices

    def find_connections(self, devices):
        connections = []
        for dev in devices:
            if dev.addrType == "random":
                phone = dev.addr
                socket = "Some socket"
                connections.append((phone, socket))
        return connections

class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr, "(", dev.addrType, ")")
        elif isNewData:
            print("Received new data from", dev.addr, "(", dev.addrType, ")")

    def handleNotification(self, cHandle, data):
        print("Notification received: Handle=", cHandle, ", Data=", data.hex())

    def handleDisconnected(self, dev, reason):
        print("Device", dev.addr, "(", dev.addrType, ") disconnected. Reason:", reason)
