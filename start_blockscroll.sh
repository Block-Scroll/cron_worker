#!/bin/bash

echo "Starting BlockScroll YouTube Auto-Uploader..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.7+ and try again"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
if ! python3 -c "import cv2, PIL, moviepy, schedule, pytz" &> /dev/null; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
fi

# Check if client_secret.json exists
if [ ! -f "client_secret.json" ]; then
    echo "Error: client_secret.json not found"
    echo "Please download your YouTube API credentials and place them in this directory"
    echo "See setup_guide.md for instructions"
    exit 1
fi

# Start the application
echo "Starting BlockScroll app..."
echo "Press Ctrl+C to stop the application"
echo
python3 main_app.py start
