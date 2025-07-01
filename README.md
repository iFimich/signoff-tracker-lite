## Signoff Flow Tracker

## 📘 Project Scope
This is a personal learning project inspired by real RTL-to-GDS signoff processes. It simulates timing (STA), area, and DRC report parsing using mock data, and adds basic ML classification for educational purposes.

The goal is to demonstrate concepts in EDA tooling, CLI automation, and test-driven Python development — not to replicate full production signoff tools.

---

## Features

- Parse PrimeTime-style timing reports
- Parse synthesis area reports
- Display a summary with slack, violations, and area
- Generate bar charts for visual inspection
- Use a pre-trained ML model to classify block quality
- Export summary to a text file

---

## 🧰 Requirements
- Python 3.7+
- Packages:
  - `matplotlib`
  - `scikit-learn`
  - `joblib`
  - `pandas`
  - `pytest`


---

## 🚀 Usage

### Example:
```bash
python3 signoff_summary_ml.py \
  --timing reports/pt_report.txt \
  --area reports/area_report.txt \
  --ml ml/model.pkl \
  --plot \
  --out summary.txt
```

### CLI Options:
| Option       | Description                                           |
|--------------|-------------------------------------------------------|
| `--timing`   | Path to the PrimeTime timing report                  |
| `--area`     | Path to the synthesis area report                    |
| `--plot`     | Show a bar chart of key metrics                      |
| `--out`      | Save the summary to a text file                      |
| `--ml`       | Path to pre-trained ML model for block prediction   |

---

## 🔬 ML Model Support

The script supports classification using a scikit-learn model trained on:
- Slack (float)
- Number of violations (int)
- Area (float)

Use the included `retrain_model.py` to generate or update a `model.pkl`.

---

## 🧪 Sample Dataset & Model
- `training_data.csv` — Sample training data
- `model.pkl` — Trained model used for prediction

---

## 📦 Output
- Printed summary in terminal
- ML prediction
- Optional plot of slack, violations, area
- Optional `.txt` summary file

---

## 🧪 Testing Support

- Includes Pytest unit tests for:
  - Real file-based integration tests
- Helps ensure reliable parsing and analysis across flows

---

## 📁 Folder Structure
```
.
├── signoff_summary_ml.py
├── terminal_utils.py
├── ML/
│   ├── retrain_model.py
│   ├── training_data.csv
│   └── model.pkl
├── reports/
│   ├── pt_report.txt
│   └── area_report.txt
├── tests/
│   └── test_signoff_data.py
└── README.md
```

---
