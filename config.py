# ============================================================================
# CONFIG.py - Centralized Configuration File
# ============================================================================
# All configurable parameters in one place
# Easy to modify for different environments/machines
# ============================================================================

import os
from pathlib import Path

# ============================================================================
# PATHS (Relative paths - works on any machine)
# ============================================================================

# Project root directory
PROJECT_ROOT = Path(__file__).parent.absolute()

# Input/Output directories
INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Data files
DATA_FILE = INPUT_DIR / "DATA.xlsx"
NASDAQ_FILE = INPUT_DIR / "NASDAQ_INDEX.xlsx"
EVENTS_FILE = INPUT_DIR / "LIST EVENT.xlsx"

# Ensure directories exist
INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# ============================================================================
# MODEL PARAMETERS
# ============================================================================

# Data date range
DATA_START_DATE = "1990-01-01"
DATA_END_DATE = "2025-12-31"

# Discount factors (DLM TVP-SV)
DISCOUNT_FACTOR_BASE = 0.995      # Normal periods
DISCOUNT_FACTOR_EVENT = 0.95      # Event periods (faster adaptation)

# Event impact window
EVENT_IMPACT_WINDOW = 10           # Trading days of impact after event

# Forecasting horizons
FORECAST_HORIZONS = [1, 2, 3, 4, 5]  # h=1-5 days ahead

# ============================================================================
# CALIBRATION PARAMETERS
# ============================================================================

# Target coverage for prediction intervals
TARGET_COVERAGE = 0.95             # 95%

# Confidence level for z-score
Z_SCORE_95 = 1.96

# Grid search for variance calibration
SCALE_MIN = 0.5
SCALE_MAX = 3.0
SCALE_STEPS = 300                  # Number of grid points

# ============================================================================
# VISUALIZATION PARAMETERS
# ============================================================================

# Figure settings
FIGURE_DPI = 300                   # Resolution (300 dpi for production)
FIGURE_FORMAT = 'png'              # Format (png, pdf, etc)

# Font sizes
TITLE_FONTSIZE = 12
LABEL_FONTSIZE = 11
TICK_FONTSIZE = 10

# Colors
COLOR_NORMAL = 'steelblue'
COLOR_EVENT = 'coral'
COLOR_ACTUAL = 'navy'
COLOR_FORECAST = 'red'

# Rolling window for metrics
ROLLING_WINDOW = 252               # Trading days (approx 1 year)

# ============================================================================
# LOGGING
# ============================================================================

# Print verbose output
VERBOSE = True

# Log file (optional)
LOG_FILE = OUTPUT_DIR / "model.log"

# ============================================================================
# DATA PROCESSING
# ============================================================================

# Macro data sheet name
MACRO_SHEET_NAME = "Sheet1"

# Events data sheet name
EVENTS_SHEET_NAME = "tóm tắt"

# Ragged-edge lag (months)
RAGGED_EDGE_LAG = 1

# Standardization window type
STANDARDIZATION_TYPE = "expanding"  # "expanding" or "rolling"

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_output_file_path(filename: str) -> str:
    """Create full path for output file"""
    return str(OUTPUT_DIR / filename)

def create_input_file_path(filename: str) -> str:
    """Create full path for input file"""
    return str(INPUT_DIR / filename)

def print_config():
    """Print current configuration"""
    print("\n" + "="*80)
    print("CONFIGURATION SUMMARY")
    print("="*80)
    print(f"\n📁 Paths:")
    print(f"   Project Root: {PROJECT_ROOT}")
    print(f"   Input Dir:    {INPUT_DIR}")
    print(f"   Output Dir:   {OUTPUT_DIR}")
    print(f"\n📊 Model:")
    print(f"   Discount Base:      {DISCOUNT_FACTOR_BASE}")
    print(f"   Discount Event:     {DISCOUNT_FACTOR_EVENT}")
    print(f"   Event Window:       {EVENT_IMPACT_WINDOW} days")
    print(f"   Forecast Horizons:  {FORECAST_HORIZONS}")
    print(f"\n📈 Calibration:")
    print(f"   Target Coverage:    {TARGET_COVERAGE*100:.0f}%")
    print(f"   Scale Grid:         {SCALE_MIN} to {SCALE_MAX} ({SCALE_STEPS} steps)")
    print(f"\n🎨 Visualization:")
    print(f"   DPI:                {FIGURE_DPI}")
    print(f"   Format:             {FIGURE_FORMAT}")
    print(f"   Rolling Window:     {ROLLING_WINDOW} days")
    print(f"\n" + "="*80 + "\n")

# ============================================================================
# USAGE IN NOTEBOOK
# ============================================================================
# 
# Instead of hardcoded paths like:
#   macro_raw = pd.read_excel('input/DATA.xlsx')
#
# Use config file:
#   from config import *
#   macro_raw = pd.read_excel(str(DATA_FILE))
#
# Benefits:
# - Single place to change all settings
# - Works on any machine
# - Easy to switch between environments
# - Reproducible and maintainable
#

if __name__ == "__main__":
    # Print configuration when running this file directly
    print_config()
