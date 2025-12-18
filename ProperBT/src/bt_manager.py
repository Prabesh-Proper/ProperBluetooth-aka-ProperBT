import subprocess
import sys
import os
from .logger import Logger

class BTManager:
    def __init__(self):
        self.logger = Logger()

    def run_command(self, cmd, sudo=False):
        """Run a system command and return output."""
        try:
            if sudo and os.geteuid() != 0:
                cmd = ['sudo'] + cmd
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Command failed: {' '.join(cmd)} - {e}")
            return None

    def detect_adapters(self):
        """Detect Bluetooth adapters."""
        self.logger.info("Detecting Bluetooth adapters...")
        output = self.run_command(['hciconfig'])
        if output:
            adapters = []
            for line in output.split('\n'):
                if line.startswith('hci'):
                    adapters.append(line.split(':')[0])
            return adapters
        return []

    def enable_services(self):
        """Enable required Bluetooth services."""
        self.logger.info("Enabling Bluetooth services...")
        services = ['bluetooth', 'bluez']
        for service in services:
            self.run_command(['sudo', 'systemctl', 'enable', service], sudo=True)
            self.run_command(['sudo', 'systemctl', 'start', service], sudo=True)

    def unblock_bluetooth(self):
        """Unblock Bluetooth if blocked by rfkill."""
        self.logger.info("Checking rfkill status...")
        output = self.run_command(['rfkill', 'list', 'bluetooth'])
        if 'blocked' in output.lower():
            self.run_command(['sudo', 'rfkill', 'unblock', 'bluetooth'], sudo=True)
            self.logger.info("Bluetooth unblocked.")

    def scan_devices(self):
        """Scan for nearby Bluetooth devices."""
        self.logger.info("Scanning for Bluetooth devices...")
        # Use bluetoothctl to scan
        try:
            process = subprocess.Popen(['bluetoothctl', 'scan', 'on'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Wait a bit for scan
            import time
            time.sleep(10)
            process.terminate()
            # Get devices
            result = subprocess.run(['bluetoothctl', 'devices'], capture_output=True, text=True)
            devices = []
            for line in result.stdout.split('\n'):
                if line.startswith('Device'):
                    parts = line.split()
                    mac = parts[1]
                    name = ' '.join(parts[2:]) if len(parts) > 2 else 'Unknown'
                    devices.append({'mac': mac, 'name': name})
            return devices
        except Exception as e:
            self.logger.error(f"Scan failed: {e}")
            return []

    def pair_device(self, mac):
        """Pair with a device."""
        self.logger.info(f"Pairing with {mac}...")
        self.run_command(['bluetoothctl', 'pair', mac])

    def trust_device(self, mac):
        """Trust a device."""
        self.logger.info(f"Trusting {mac}...")
        self.run_command(['bluetoothctl', 'trust', mac])

    def connect_device(self, mac):
        """Connect to a device."""
        self.logger.info(f"Connecting to {mac}...")
        self.run_command(['bluetoothctl', 'connect', mac])

    def disconnect_device(self, mac):
        """Disconnect from a device."""
        self.logger.info(f"Disconnecting from {mac}...")
        self.run_command(['bluetoothctl', 'disconnect', mac])

    def remove_device(self, mac):
        """Remove a device."""
        self.logger.info(f"Removing {mac}...")
        self.run_command(['bluetoothctl', 'remove', mac])

    def get_connected_devices(self):
        """Get list of connected devices."""
        output = self.run_command(['bluetoothctl', 'info'])
        # Parse connected devices
        connected = []
        if output:
            for line in output.split('\n'):
                if 'Connected: yes' in line:
                    # Assuming previous line has device info, but simplify
                    pass
        return connected  # Placeholder, need better parsing
