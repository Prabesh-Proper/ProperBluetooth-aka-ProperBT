#!/bin/bash
# ProperBT Install Script

echo "Installing ProperBT..."

# Install dependencies
sudo apt update
sudo apt install -y bluetooth bluez bluez-tools python3 python3-pip

# Install Python requirements (if any)
if [ -f requirements.txt ]; then
    pip3 install -r requirements.txt
fi

# Copy executable to /usr/bin/
sudo cp properbt /usr/bin/properbt
sudo chmod +x /usr/bin/properbt

echo "Installation complete. Run 'sudo properbt' to start."
