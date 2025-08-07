#!/bin/bash

echo "Setting up Python environment for macOS 🍎"

if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ This script is designed for macOS. Detected: $OSTYPE"
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed."
    exit 1
fi

echo "Operating system: macOS"
echo "Python version: $(python3 --version)"

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing macOS-compatible dependencies..."
pip install -r config/requirements-macos-m3.txt

echo "macOS setup complete!"
