# COMPLETE EXECUTION GUIDE
## Rasaswadaya GNN - Updated System with Real Artists

---

## 🎯 OVERVIEW

This guide provides step-by-step instructions to:
1. ✅ Generate new training data with updated taxonomy
2. ✅ Export datasets to CSV format
3. ✅ Integrate real Sri Lankan artists 
4. ✅ Train GNN model with 138D Cultural DNA
5. ✅ Run full demo pipeline

---

## 📋 SYSTEM REQUIREMENTS

### Required Python Packages
```bash
# Core requirements
pip install numpy pandas

# For full training (optional)
pip install torch torch-geometric networkx scipy scikit-learn matplotlib
```

### System Specs
- Python 3.8+
- 4GB RAM minimum (8GB recommended for training)
- macOS, Linux, or Windows

---

## 🚀 STEP-BY-STEP EXECUTION

### **STEP 1: Generate New Dataset**
```bash
cd rasaswadaya_gnn
python3 generate_new_data.py
```

**Output:**
- `data/sample_dataset/rasaswadaya_dataset_updated.json`
- `data/sample_dataset/rasaswadaya_dataset_updated.pkl`
- 200 users, 100 artists, 150 events

**Expected Time:** ~30 seconds

---

### **STEP 2: Integrate Real Artists**
```bash
python3 integrate_real_artists.py
```

**Adds 15 real Sri Lankan artists:**
- W.D. Amaradeva (1.5M followers, classical music)
- Yohani (5.2M followers, viral pop)
- Bathiya & Santhush (1.2M, Grammy nominated)
- Chitrasena (450K, dance legend)
- Lester James Peries (520K, cinema father)
- And 10 more...

**Output:**
- `data/sample_dataset/rasaswadaya_dataset_with_real_artists.json`

**Expected Time:** ~5 seconds

---

### **STEP 3: Export to CSV**
```bash
python3 export_to_csv.py
```

**Output:** `data/sample_dataset/csv_export_updated/`
- `users.csv` (200 rows)
- `artists.csv` (115 rows: 100 generated + 15 real)
- `events.csv` (150 rows)
- `follows.csv` (~400 relationships)
- `attends.csv` (~300 relationships)

**Expected Time:** ~10 seconds

---

### **STEP 4: Run Training Pipeline**
```bash
python3 train_model.py
```

**What it does:**
- Loads dataset with real artists
- Builds heterogeneous graph
- Encodes Cultural DNA (138D vectors)
- Prepares for training
- Shows model architecture

**Expected Time:** ~20 seconds (without full training)

---

### **STEP 5: Run Full Demo (Optional)**
```bash
# Install PyTorch Geometric first
pip install torch torch-geometric

# Run full training and recommendation
python3 demo.py
```

**What it does:**
- Trains GNN model with 138D Cultural DNA
- Generates artist recommendations
- Performs link prediction
- Creates visualizations
- Saves trained model

**Expected Time:** 5-15 minutes (depending on hardware)

---

## 📊 AUTOMATED EXECUTION (ALL AT ONCE)

### Option A: Run All Steps Sequentially
```bash
#!/bin/bash
# File: run_all_steps.sh

cd rasaswadaya_gnn

echo "Step 1: Generating dataset..."
python3 generate_new_data.py

echo "Step 2: Integrating real artists..."
python3 integrate_real_artists.py

echo "Step 3: Exporting to CSV..."
python3 export_to_csv.py

echo "Step 4: Running training pipeline..."
python3 train_model.py

echo "✅ All steps complete!"
```

**Usage:**
```bash
chmod +x run_all_steps.sh
./run_all_steps.sh
```

### Option B: Python Master Script
```bash
python3 run_all.py
```
(Creates combined execution script)

---

## 📁 GENERATED FILES STRUCTURE

After running all steps:
```
rasaswadaya_gnn/
├── data/
│   └── sample_dataset/
│       ├── rasaswadaya_dataset_updated.json          ← Step 1
│       ├── rasaswadaya_dataset_updated.pkl          ← Step 1
│       ├── rasaswadaya_dataset_with_real_artists.json ← Step 2
│       └── csv_export_updated/                       ← Step 3
│           ├── users.csv
│           ├── artists.csv
│           ├── events.csv
│           ├── follows.csv
│           └── attends.csv
├── checkpoints/
│   └── best_model.pt                                 ← Step 5 (if trained)
└── results/
    └── recommendations.json                          ← Step 5 (if trained)
```

---

## 🔍 VERIFICATION

### Check Dataset Generated Correctly
```python
import json

# Load dataset
with open('data/sample_dataset/rasaswadaya_dataset_with_real_artists.json') as f:
    data = json.load(f)

print(f"Users: {len(data['users'])}")           # Should be 200
print(f"Artists: {len(data['artists'])}")       # Should be 115 (100+15)
print(f"Events: {len(data['events'])}")         # Should be 150

# Check for real artists
real_artists = [a for a in data['artists'] if a.get('era') == 'legend']
print(f"Real legendary artists: {len(real_artists)}")

# Sample real artist
yohani = [a for a in data['artists'] if a['name'] == 'Yohani'][0]
print(f"\nYohani followers: {yohani['follower_count']:,}")  # 5,200,000
```

### Check CSV Export
```bash
# View CSV files
head -n 5 data/sample_dataset/csv_export_updated/artists.csv

# Count rows
wc -l data/sample_dataset/csv_export_updated/*.csv
```

### Verify Cultural DNA Dimensions
```python
from models.cultural_dna import CulturalDNAEncoder

encoder = CulturalDNAEncoder()
print(f"Cultural DNA dimensions: {encoder.total_dims}")  # Should be 138
```

---

## 📈 DATASET STATISTICS

After generation, you should see:

### Artists by Art Form:
- **Music**: ~40-50 artists (40-45%)
- **Dance**: ~20-30 artists (20-25%)
- **Film**: ~20-30 artists (20-25%)
- **Drama**: ~15-25 artists (15-20%)

### Artists by Language:
- **Sinhala**: ~70-80 artists
- **Tamil**: ~15-20 artists
- **English**: ~10-15 artists
- **Bilingual**: ~10-20 artists

### Real Artists Included:
1. W.D. Amaradeva - Classical Music Legend
2. Nanda Malini - Devotional Songs
3. Yohani - Viral Pop Sensation (5.2M followers)
4. Bathiya & Santhush - Grammy Nominated Duo
5. Rookantha Gunathilaka - Pop Ballads
6. Costa - Hip Hop Pioneer
7. Sunil Perera - Baila King (Gypsies)
8. Chitrasena - Dance Legend
9. Vajira Chitrasena - Dance Icon
10. Lester James Peries - Cinema Father
11. Jackson Anthony - Film & Drama Star
12. Ediriweera Sarachchandra - Theatre Revival
13. Sanuka Wickramasinghe - Contemporary Ballads
14. Iraj Weeraratne - Fusion Hip Hop
15. Umaria Sinhawansa - Pop Singer

---

## 🎯 NEXT STEPS AFTER GENERATION

### 1. Explore Data
```python
import pandas as pd

# Load CSV
artists = pd.read_csv('data/sample_dataset/csv_export_updated/artists.csv')

# Explore
print(artists.head())
print(artists['art_forms'].value_counts())
print(artists.sort_values('follower_count', ascending=False).head(10))
```

### 2. Visualize Statistics
```python
import matplotlib.pyplot as plt

# Art form distribution
artists['art_forms'].value_counts().plot(kind='bar')
plt.title('Artists by Art Form')
plt.show()
```

### 3. Start Training
```bash
python3 demo.py
```

### 4. Use for Recommendations
The trained model will recommend:
- Artists based on user preferences
- Events based on user location and interests
- Similar artists using Cultural DNA similarity

---

## ⚠️ TROUBLESHOOTING

### Issue: "Module not found" errors
**Solution:**
```bash
pip install numpy pandas
```

### Issue: Dataset not found
**Solution:**
```bash
# Make sure you're in the correct directory
cd rasaswadaya_gnn

# Re-run generation
python3 generate_new_data.py
```

### Issue: CSV export fails
**Solution:**
```bash
# Check if JSON file exists
ls -lh data/sample_dataset/rasaswadaya_dataset_updated.json

# Re-run if needed
python3 generate_new_data.py
python3 export_to_csv.py
```

### Issue: Training fails (PyTorch)
**Solution:**
```bash
# Install PyTorch first
pip install torch torch-geometric

# Or use CPU-only version
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

---

## 📞 SUPPORT & DOCUMENTATION

- **Quick Reference**: `QUICK_REFERENCE.md`
- **System Update**: `SYSTEM_UPDATE_SUMMARY.md`
- **Implementation Guide**: `IMPLEMENTATION_GUIDE.md`
- **Real Artists Database**: `COMPLETE_CULTURAL_DATABASE_2026.md`

---

## ✅ SUCCESS CHECKLIST

- [ ] Step 1: Dataset generated (200 users, 100 artists, 150 events)
- [ ] Step 2: Real artists integrated (15 legendary/contemporary artists)
- [ ] Step 3: CSV files exported (5 files in csv_export_updated/)
- [ ] Step 4: Training pipeline configured (138D Cultural DNA)
- [ ] Step 5: Model trained (optional - requires PyTorch)

---

**Status**: Ready to execute
**Version**: 2.0 (Updated Cultural Database)  
**Date**: February 25, 2026
