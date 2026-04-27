# PiCloud - Personal Local Cloud Storage

PiCloud is an initial prototype for a self-hosted, local-first personal cloud storage system designed to run on a Raspberry Pi using an external SSD.

This repository contains a basic FastAPI backend file server and an HTML/JS web interface that allows you to upload, view, download, and delete files securely on your local network.

## Prerequisites

- A Raspberry Pi running a Debian-based OS (like Raspberry Pi OS).
- Python 3 installed.
- (Optional) An external SSD connected via USB.

## Installation

A `setup.sh` script is provided to automate the installation of dependencies and creation of a Python virtual environment.

1. Make the setup script executable:
   ```bash
   chmod +x setup.sh
   ```

2. Run the setup script:
   ```bash
   ./setup.sh
   ```

This script will:
- Update the system's package list.
- Install necessary system dependencies (Python3 venv, ufw, ntfs-3g, exfat-fuse).
- Create a Python virtual environment (`.venv`).
- Install Python dependencies (FastAPI, Uvicorn, aiosqlite, aiofiles, etc.).
- Attempt to create the storage directory `/mnt/picloud_storage` for your files.

*Note: If the script does not have permissions to write to `/mnt`, the application will automatically fallback to creating a `picloud_storage` directory in the current working directory.*

## Running the Server

Once setup is complete, you can start the PiCloud server:

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

2. Change into the `picloud` directory and start the server:
   ```bash
   cd picloud
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
   (Alternatively, use `--reload` instead of `--host` for local development).

The server will now be accessible from your local network.

## Usage

Open a web browser and navigate to the IP address of your Raspberry Pi on port 8000 (e.g., `http://192.168.1.100:8000` or `http://localhost:8000` if testing locally).

You will be greeted with a login screen.

**Default Credentials:**
- **Username:** `admin`
- **Password:** `admin`

After logging in, you can drag and drop files into the designated area or use the file selector to upload them to your PiCloud storage. Your uploaded files will appear in a list below, where they can be downloaded or deleted.

## Future Roadmap

This is an early prototype (v0.1) addressing basic file server capabilities. The requested roadmap includes:
- Automated external SSD mounting.
- Sub-folder organization and search functionality.
- Mobile application (Android/iOS) with QR code pairing.
- Automated media syncing and backup.
- Built-in media streaming viewers.
- Expanded multi-user authentication.
