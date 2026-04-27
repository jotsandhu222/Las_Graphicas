#!/bin/bash
# Setup script for PiCloud on Raspberry Pi

echo "Setting up PiCloud..."

# Update system
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv ufw ntfs-3g exfat-fuse

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install fastapi uvicorn python-multipart aiosqlite aiofiles passlib bcrypt==3.2.2 jinja2 websockets

# Setup storage directory for external SSD (placeholder path, script will mount)
STORAGE_DIR="/mnt/picloud_storage"
if [ ! -d "$STORAGE_DIR" ]; then
    sudo mkdir -p "$STORAGE_DIR"
    sudo chown -R $USER:$USER "$STORAGE_DIR"
fi

echo "Setup complete. To run the server:"
echo "source .venv/bin/activate"
echo "cd picloud && uvicorn main:app --host 0.0.0.0 --port 8000"
