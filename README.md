# 🚀 NASDAQ Forecasting Model - Quick Setup & Run

Production-ready NASDAQ forecasting with DLM TVP-SV model. **Chạy được trên mọi máy!**

---

## ⚡ Quick Start (10 phút)

### 1️⃣ Setup Environment

**Windows:**
```bash
setup.bat
```

**Linux/macOS:**
```bash
chmod +x setup.sh
./setup.sh
```

### 2️⃣ Add Input Data

Tạo thư mục `input/` và đặt 2 file vào:
```
input/
├── DATA.xlsx          (Macro indicators - required)
└── LIST EVENT.xlsx    (Fed events - required)
```

### 3️⃣ Run Model

```bash
# Activate environment
.venv\Scripts\activate              # Windows
source .venv/bin/activate           # Linux/macOS

# Start notebook
jupyter notebook Model_Fixed_Optimized.ipynb
```

**Trong Jupyter:**
- Chọn Kernel → `.venv`
- Chạy tất cả: `Ctrl+A` → `Ctrl+Shift+Enter`
- Chờ ~10 phút

### 4️⃣ Check Results

Kết quả trong `output/` folder:
- `calibration_result.csv` - Metrics
- `walk_forward_results.csv` - Forecasts
- `multistep_result.csv` - Multi-step metrics
- `01_*` to `10_*.png` - 10 visualization charts

✅ **DONE!**

---

## 📦 File Structure

```
NCKH/
├── Model_Fixed_Optimized.ipynb    ← Main model (run this!)
├── requirements.txt                ← Python dependencies
├── setup.bat & setup.sh            ← Auto setup
├── config.py                       ← Settings (modify if needed)
├── .gitignore                      ← Git control
├── README.md                       ← This file
├── input/                          ← Put your input files here
└── output/                         ← Results auto-generate here
```

---

## 🔧 System Requirements

- Python 3.10+
- 2 GB RAM (minimum)
- 500 MB disk space
- Internet connection (for data download)

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| "Python not found" | Install Python 3.10+ from python.org |
| "Module not found" | Run: `pip install -r requirements.txt` |
| "File not found" | Check input files in `input/` folder |
| "Permission denied" (Linux) | Run: `chmod +x setup.sh` |

---

## 📖 Documentation

- **config.py** - Modify model parameters here
- **Model_Fixed_Optimized.ipynb** - Full model code with explanations
- **requirements.txt** - Python packages needed

---

## ✨ What This Model Does

✅ **NASDAQ Forecasting** - Daily return predictions (h=1-5 days)
✅ **Macro Integration** - Uses economic indicators (FCI)
✅ **Event-Aware** - Adjusts for Fed policy changes
✅ **No Look-Ahead Bias** - Respects causality, no data leakage
✅ **Event-Specific Calibration** - Separate models for normal/event periods
✅ **Multiple Metrics** - RMSE, MAE, MAPE, DTW

---

## 🎯 Key Features

- **DLM TVP-SV Model** - Dynamic Linear Model with Time-Varying Parameters
- **Recursive Least Squares** - RLS filtering for online learning
- **Two-Tier Discount** - δ=0.995 (normal), δ=0.95 (events)
- **Ragged-Edge Macro** - Monthly data delayed 1 month (no look-ahead)
- **Expanding Window Standardization** - Only past data used for normalization
- **95% Coverage Target** - Both normal and event regimes calibrated

---

## 💡 Usage

**Change Parameters:**
```python
# Edit config.py:
DISCOUNT_FACTOR_BASE = 0.995    # Normal periods
DISCOUNT_FACTOR_EVENT = 0.95    # Event periods
EVENT_IMPACT_WINDOW = 10        # Trading days
```

**Run on Different Machine:**
1. Copy all source files (not .venv, not output/)
2. Run `setup.bat` or `setup.sh`
3. Place input files
4. Run `jupyter notebook Model_Fixed_Optimized.ipynb`

✅ Works everywhere! (Windows, Linux, macOS)

---

## 📊 Output Files

### CSV Files
- **calibration_result.csv** - Model metrics by regime
- **walk_forward_results.csv** - Forecasts with errors and regimes
- **multistep_result.csv** - Multi-step metrics (h=1-5)

### Visualization Charts (PNG)
1. Time series (actual vs forecast)
2. Error distribution
3. Performance metrics
4. Actual vs forecast scatter
5. Rolling metrics (252-day MA)
6. Regime comparison
7. Time series by regime
8. Calibration details
9. MAPE metrics
10. DTW metrics

---

## ✅ Status

🟢 **Production Ready**
- Tested on Windows, Linux, macOS
- All dependencies auto-installed
- Relative paths (works anywhere)
- 95% coverage targets met
- No look-ahead bias verified

---

**Need help?**
- Read code comments in Model_Fixed_Optimized.ipynb
- Check config.py for parameter explanations
- Run setup script for automatic installation

Happy forecasting! 📈
