# scanner.py

from bluepy.btle import Scanner, DefaultDelegate, BTLEException, Peripheral
import time

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

    def flood_connections(self, device_address, attempts=100):
        for i in range(attempts):
            try:
                peripheral = Peripheral(device_address)
                print(f"Attempt {i + 1}: Connected to {device_address}")
                # Example: Perform any required operations with the socket here
                # Example: socket.send(b"Hello from BluetoothScanner!")
                peripheral.disconnect()
                print(f"Attempt {i + 1}: Disconnected from {device_address}")
            except BTLEException as e:
                print(f"Attempt {i + 1}: Failed to connect: {e}")
            time.sleep(0.1)  # Small delay between attempts

class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print(f"Discovered device {dev.addr} ({dev.addrType})")

    def handleNotification(self, cHandle, data):
        print(f"Notification received: Handle={cHandle}, Data={data.hex()}")

    def handleDisconnected(self, dev, reason):
        print(f"Device {dev.addr} ({dev.addrType}) disconnected. Reason: {reason}")
