# 🚀 QUICK START - View Your Generated Data

## ✅ What Was Generated

**3 complete steps executed successfully:**

1. ✅ **Dataset Generated**: 200 users, 100 artists, 150 events
2. ✅ **Real Artists Added**: 15 legendary Sri Lankan artists (W.D. Amaradeva, Yohani, Chitrasena, etc.)  
3. ✅ **CSV Exported**: 5 CSV files ready for analysis

---

## 📊 View Your Data (Copy & Paste)

### Option 1: View CSV Files
```bash
cd "/Users/akilanishan/Desktop/AI Model/rasaswadaya_gnn"

# List all CSV files
ls -lh data/sample_dataset/csv_export_updated/

# View artists (first 10 rows)
head -10 data/sample_dataset/csv_export_updated/artists.csv

# View users (first 10 rows)
head -10 data/sample_dataset/csv_export_updated/users.csv

# View events
head -10 data/sample_dataset/csv_export_updated/events.csv

# Count total rows
wc -l data/sample_dataset/csv_export_updated/*.csv
```

### Option 2: Use Python/Pandas
```bash
cd "/Users/akilanishan/Desktop/AI Model/rasaswadaya_gnn"
"/Users/akilanishan/Desktop/AI Model/.venv/bin/python"
```

Then in Python:
```python
import pandas as pd
import json

# Load CSV files
artists = pd.read_csv('data/sample_dataset/csv_export_updated/artists.csv')
users = pd.read_csv('data/sample_dataset/csv_export_updated/users.csv')
events = pd.read_csv('data/sample_dataset/csv_export_updated/events.csv')

# View first few rows
print("ARTISTS:")
print(artists.head())
print(f"\nTotal artists: {len(artists)}")

print("\n\nUSERS:")
print(users.head())
print(f"\nTotal users: {len(users)}")

print("\n\nEVENTS:")
print(events.head())
print(f"\nTotal events: {len(events)}")

# Art form distribution
print("\n\nARTISTS BY ART FORM:")
print(artists['art_forms'].value_counts())

# Exit Python
exit()
```

### Option 3: View Real Artists (JSON)
```bash
cd "/Users/akilanishan/Desktop/AI Model/rasaswadaya_gnn"
"/Users/akilanishan/Desktop/AI Model/.venv/bin/python" << 'EOF'
import json

# Load dataset with real artists
with open('data/sample_dataset/rasaswadaya_dataset_with_real_artists.json') as f:
    data = json.load(f)

# Find real artists (have 'era' field)
real_artists = [a for a in data['artists'] if a.get('era') in ['legend', 'contemporary']]

print(f"Total artists: {len(data['artists'])}")
print(f"Real artists: {len(real_artists)}")
print(f"Generated artists: {len(data['artists']) - len(real_artists)}")

print("\n" + "="*60)
print("REAL SRI LANKAN ARTISTS (Top 10 by Followers)")
print("="*60)

# Sort by followers and display
sorted_artists = sorted(real_artists, key=lambda x: x.get('follower_count', 0), reverse=True)
for i, artist in enumerate(sorted_artists[:10], 1):
    name = artist['name']
    followers = artist.get('follower_count', 0)
    art_form = artist['art_form']
    era = artist.get('era', 'unknown')
    print(f"{i:2}. {name:30} | {followers:>10,} followers | {art_form:6} | {era}")

print("\n" + "="*60)
EOF
```

---

## 🎯 Next Steps

### 1. Explore Data in Excel/Numbers
```bash
# Open CSV in your spreadsheet app
open data/sample_dataset/csv_export_updated/artists.csv
open data/sample_dataset/csv_export_updated/users.csv
open data/sample_dataset/csv_export_updated/events.csv
```

### 2. Install PyTorch & Train Model
```bash
cd "/Users/akilanishan/Desktop/AI Model/rasaswadaya_gnn"

# Install PyTorch dependencies (optional, for training)
"/Users/akilanishan/Desktop/AI Model/.venv/bin/python" -m pip install torch torch-geometric

# Run training pipeline
"/Users/akilanishan/Desktop/AI Model/.venv/bin/python" train_model.py
```

### 3. Run Full Demo
```bash
cd "/Users/akilanishan/Desktop/AI Model/rasaswadaya_gnn"
"/Users/akilanishan/Desktop/AI Model/.venv/bin/python" demo.py
```

---

## 📁 Files Generated

```
data/sample_dataset/
├── rasaswadaya_dataset_updated.json              (712 KB) - Full dataset
├── rasaswadaya_dataset_updated.pkl              (247 KB) - Pickle format
├── rasaswadaya_dataset_with_real_artists.json   (723 KB) - With 15 real artists
└── csv_export_updated/
    ├── users.csv          (200 rows)  - User profiles
    ├── artists.csv        (100 rows)  - Artist profiles  
    ├── events.csv         (150 rows)  - Events
    ├── follows.csv        (1,684 rows) - User→Artist follows
    └── attends.csv        (973 rows)  - User→Event attendance
```

---

## 🎨 Real Artists Included

1. **Yohani** - 5.2M followers (Pop, "Manike Mage Hithe")
2. **W.D. Amaradeva** - 1.5M followers (Classical Legend)
3. **Bathiya & Santhush** - 1.2M followers (Grammy Nominated)
4. **Rookantha Gunathilaka** - 900K followers (Pop Ballads)
5. **Jackson Anthony** - 900K followers (Film & Drama)
6. **Nanda Malini** - 850K followers (Devotional)
7. **Sunil Perera** - 800K followers (Baila - The Gypsies)
8. **Lester James Peries** - 520K followers (Cinema Father)
9. **Chitrasena** - 450K followers (Dance Legend)
10. **Sanuka Wickramasinghe** - 450K followers (Contemporary)
11. **Vajira Chitrasena** - 420K (Dance Icon)
12. **Costa** - 380K (Hip Hop Pioneer)
13. **Ediriweera Sarachchandra** - 320K (Theatre)
14. **Iraj Weeraratne** - 410K (Fusion Hip Hop)
15. **Umaria Sinhawansa** - 390K (Pop)

---

## 📚 Documentation

- **COMPLETION_REPORT.md** - Full success report with statistics
- **EXECUTION_GUIDE.md** - Step-by-step execution instructions
- **QUICK_REFERENCE.md** - System overview and taxonomy
- **SYSTEM_UPDATE_SUMMARY.md** - Technical update details

---

## ✅ Status

**ALL CRITICAL STEPS COMPLETE!**

You now have:
- ✅ 200 user profiles
- ✅ 115 artists (100 generated + 15 real)
- ✅ 150 events
- ✅ 1,684 follow relationships
- ✅ 973 attendance records
- ✅ 5 CSV files ready for analysis
- ✅ 138D Cultural DNA system configured

**Ready for GNN model training!**

---

_Quick Start Guide - February 25, 2026_
