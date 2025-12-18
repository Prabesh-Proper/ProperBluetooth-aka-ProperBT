import os
import sys
from .bt_manager import BTManager

class CLIMenu:
    def __init__(self):
        self.bt = BTManager()
        self.devices = []

    def display_banner(self):
        print("Made by Proper © | Kali Linux Bluetooth Tool")
        print("=" * 50)

    def main_menu(self):
        while True:
            self.display_banner()
            print("1. Detect Adapters")
            print("2. Enable Services")
            print("3. Unblock Bluetooth")
            print("4. Scan Devices")
            print("5. Pair Device")
            print("6. Trust Device")
            print("7. Connect Device")
            print("8. Disconnect Device")
            print("9. Remove Device")
            print("10. Show Connected Devices")
            print("0. Exit")
            choice = input("Choose an option: ").strip()
            self.handle_choice(choice)

    def handle_choice(self, choice):
        if choice == '1':
            adapters = self.bt.detect_adapters()
            print(f"Adapters: {adapters}")
        elif choice == '2':
            self.bt.enable_services()
            print("Services enabled.")
        elif choice == '3':
            self.bt.unblock_bluetooth()
            print("Bluetooth unblocked.")
        elif choice == '4':
            self.devices = self.bt.scan_devices()
            print("Devices found:")
            for i, dev in enumerate(self.devices):
                print(f"{i+1}. {dev['name']} ({dev['mac']})")
        elif choice == '5':
            mac = self.select_device()
            if mac:
                self.bt.pair_device(mac)
                print("Paired.")
        elif choice == '6':
            mac = self.select_device()
            if mac:
                self.bt.trust_device(mac)
                print("Trusted.")
        elif choice == '7':
            mac = self.select_device()
            if mac:
                self.bt.connect_device(mac)
                print("Connected.")
        elif choice == '8':
            mac = self.select_device()
            if mac:
                self.bt.disconnect_device(mac)
                print("Disconnected.")
        elif choice == '9':
            mac = self.select_device()
            if mac:
                self.bt.remove_device(mac)
                print("Removed.")
        elif choice == '10':
            connected = self.bt.get_connected_devices()
            print(f"Connected: {connected}")
        elif choice == '0':
            sys.exit(0)
        else:
            print("Invalid choice.")
        input("Press Enter to continue...")

    def select_device(self):
        if not self.devices:
            print("No devices scanned. Scan first.")
            return None
        for i, dev in enumerate(self.devices):
            print(f"{i+1}. {dev['name']} ({dev['mac']})")
        idx = int(input("Select device number: ")) - 1
        if 0 <= idx < len(self.devices):
            return self.devices[idx]['mac']
        return None

if __name__ == '__main__':
    menu = CLIMenu()
    menu.main_menu()
