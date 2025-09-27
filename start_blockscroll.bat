@echo off
echo Starting BlockScroll YouTube Auto-Uploader...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
pip show opencv-python >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Check if client_secret.json exists
if not exist "client_secret.json" (
    echo Error: client_secret.json not found
    echo Please download your YouTube API credentials and place them in this directory
    echo See setup_guide.md for instructions
    pause
    exit /b 1
)

REM Start the application
echo Starting BlockScroll app...
echo Press Ctrl+C to stop the application
echo.
python main_app.py start

pause
