#!/bin/bash
# ============================================================================
# NASDAQ FORECAST - AUTO SETUP SCRIPT (Linux/macOS)
# ============================================================================
# This script sets up the project environment on any Linux/macOS machine
# ============================================================================

echo ""
echo "============================================================================"
echo "NASDAQ FORECAST - AUTOMATIC SETUP (Linux/macOS)"
echo "============================================================================"
echo ""

# Check Python installation
echo "[1/5] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed"
    echo "Please install Python 3.10+ first"
    exit 1
fi
python3 --version
echo "    ✓ Python found"

# Create virtual environment
echo ""
echo "[2/5] Creating virtual environment..."
if [ -d ".venv" ]; then
    echo "    ✓ Virtual environment already exists"
else
    python3 -m venv .venv
    echo "    ✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "[3/5] Activating virtual environment..."
source .venv/bin/activate
echo "    ✓ Virtual environment activated"

# Install requirements
echo ""
echo "[4/5] Installing dependencies (pandas, numpy, yfinance, etc.)..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt
echo "    ✓ All dependencies installed"

# Create input/output directories
echo ""
echo "[5/5] Creating input/output directories..."
mkdir -p input
mkdir -p output
echo "    ✓ Directories ready"

echo ""
echo "============================================================================"
echo "✓ SETUP COMPLETE!"
echo "============================================================================"
echo ""
echo "Next steps:"
echo "  1. Make sure input/ folder contains:"
echo "     - DATA.xlsx"
echo "     - NASDAQ_INDEX.xlsx"
echo "     - LIST EVENT.xlsx"
echo ""
echo "  2. Run the notebook:"
echo "     jupyter notebook Model_Fixed_Optimized.ipynb"
echo ""
echo "  3. Select kernel: .venv (Python 3.x)"
echo ""
echo "============================================================================"
