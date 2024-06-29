from service.scanner import BluetoothScanner

def main():
    scanner = BluetoothScanner()
    devices = scanner.scan_devices()

    # Find connections (phones) and flood connections example
    connections = scanner.find_connections(devices)
    for phone, socket in connections:
        print(f"Phone: {phone}, Socket: {socket}")
        scanner.flood_connections(phone)

if __name__ == "__main__":
    main()
