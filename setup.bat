@echo off
REM ============================================================================
REM NASDAQ FORECAST - AUTO SETUP SCRIPT (Windows)
REM ============================================================================
REM This script sets up the project environment on any Windows machine
REM ============================================================================

setlocal enabledelayedexpansion

echo.
echo ============================================================================
echo NASDAQ FORECAST - AUTOMATIC SETUP
echo ============================================================================
echo.

REM Check Python installation
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10+ from https://www.python.org
    pause
    exit /b 1
)
echo     ✓ Python found

REM Create virtual environment
echo.
echo [2/5] Creating virtual environment...
if exist .venv (
    echo     ✓ Virtual environment already exists
) else (
    python -m venv .venv
    echo     ✓ Virtual environment created
)

REM Activate virtual environment
echo.
echo [3/5] Activating virtual environment...
call .venv\Scripts\activate.bat
echo     ✓ Virtual environment activated

REM Install requirements
echo.
echo [4/5] Installing dependencies (pandas, numpy, yfinance, etc.)...
pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if errorlevel 1 (
    echo WARNING: Some packages failed to install
) else (
    echo     ✓ All dependencies installed
)

REM Create input/output directories
echo.
echo [5/5] Creating input/output directories...
if not exist input mkdir input
if not exist output mkdir output
echo     ✓ Directories ready

echo.
echo ============================================================================
echo ✓ SETUP COMPLETE!
echo ============================================================================
echo.
echo Next steps:
echo   1. Make sure input/ folder contains:
echo      - DATA.xlsx
echo      - NASDAQ_INDEX.xlsx
echo      - LIST EVENT.xlsx
echo.
echo   2. Run the notebook:
echo      jupyter notebook Model_Fixed_Optimized.ipynb
echo.
echo   3. Select kernel: .venv (Python 3.x)
echo.
echo ============================================================================
pause
