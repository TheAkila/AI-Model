# Rasaswadaya.lk GNN Model - Quick Start Guide

## 🚀 Running the Demo

### Option 1: Automated Setup (Recommended)

```bash
cd /Users/akilanishan/Desktop/AI\ Model/rasaswadaya_gnn
chmod +x run_demo.sh
./run_demo.sh
```

### Option 2: Manual Setup

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install --upgrade pip
pip install torch numpy pandas networkx scikit-learn matplotlib seaborn tqdm

# 3. Install PyTorch Geometric (Important!)
pip install torch-geometric

# 4. Run the demo
python demo.py
```

## 📊 What the Demo Does

The demo script demonstrates the complete pipeline:

1. **Data Generation** - Creates 150 users, 60 artists, 120 events with realistic Sri Lankan cultural metadata
2. **Graph Construction** - Builds heterogeneous graph with 5 node types and multiple edge types
3. **GNN Training** - Trains GraphSAGE model for 100 epochs with link prediction
4. **Recommendations** - Generates top-5 artist and event recommendations for a sample user
5. **Explainability** - Shows why recommendations were made using Cultural DNA similarity
6. **Trend Detection** - Identifies trending artists based on recent engagement

## 📁 Output Files

After running, you'll have:

- `data/sample_dataset/rasaswadaya_dataset.json` - Generated dataset in JSON format
- `data/sample_dataset/rasaswadaya_dataset.pkl` - Dataset in pickle format (faster loading)
- `checkpoints/best_model.pt` - Trained GNN model weights

## 🧪 Testing Individual Components

### Test Cultural DNA Encoder
```bash
python models/cultural_dna.py
```

### Test Data Generation
```bash
python data/generate_sample_data.py
```

### Test Graph Builder
```bash
python models/graph_builder.py
```

### Test GNN Model
```bash
python models/gnn_model.py
```

## 🔧 Configuration

Edit `config.py` to customize:

- Number of GNN layers (default: 2)
- Hidden dimensions (default: 64)
- Training epochs (default: 100)
- Learning rate (default: 0.01)
- Model type: "graphsage" or "gat"

## 📈 Expected Results

After training, you should see:

- **Validation Accuracy**: ~70-80% (link prediction)
- **Test Accuracy**: ~65-75%
- **Training Time**: ~2-5 minutes on CPU, ~30 seconds on GPU

## 🎯 Next Steps

1. **Customize Data**: Modify `data/generate_sample_data.py` to add more realistic patterns
2. **Try GAT Model**: Change `model_type` to "gat" in `config.py` for attention-based GNN
3. **Add More Tasks**: Implement node classification or graph-level tasks
4. **Visualize**: Add graph visualization using NetworkX and Matplotlib
5. **Deploy**: Build a REST API using Flask/FastAPI for production use

## 🐛 Troubleshooting

### PyTorch Geometric Installation Issues

If you encounter issues installing PyTorch Geometric:

```bash
# For CPU-only version
pip install torch torchvision torchaudio
pip install pyg-lib torch-scatter torch-sparse torch-cluster torch-spline-conv -f https://data.pyg.org/whl/torch-2.0.0+cpu.html
pip install torch-geometric

# For CUDA 11.8 (adjust for your CUDA version)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install pyg-lib torch-scatter torch-sparse torch-cluster torch-spline-conv -f https://data.pyg.org/whl/torch-2.0.0+cu118.html
pip install torch-geometric
```

### Memory Issues

If you run out of memory:

1. Reduce batch size in `config.py`
2. Use fewer GNN layers
3. Reduce hidden dimensions
4. Generate smaller dataset

### Import Errors

Make sure you're in the correct directory:

```bash
cd /Users/akilanishan/Desktop/AI\ Model/rasaswadaya_gnn
python demo.py
```

## 📚 Research Paper Sections

This implementation covers key components for your thesis:

1. **Chapter 3: Methodology**
   - Cultural DNA Mapping algorithm
   - Heterogeneous graph construction
   - GNN architecture design

2. **Chapter 4: Implementation**
   - PyTorch Geometric framework
   - Training pipeline
   - Evaluation metrics

3. **Chapter 5: Results**
   - Link prediction accuracy
   - Recommendation quality
   - Explainability examples
   - Trend detection performance

4. **Chapter 6: Discussion**
   - Cold-start handling via Cultural DNA
   - Explainability vs black-box models
   - Scalability considerations
   - Cultural context benefits

## 🎓 Academic Contribution

**Novel aspects for your paper:**

1. **Cultural DNA Mapping** - Structured, explainable feature space for cultural metadata
2. **Heterogeneous GNN** - Multi-relational graph for cultural platforms
3. **Domain-specific Case Study** - First GNN application to Sri Lankan arts platform
4. **Explainable Recommendations** - Cultural dimension-level similarity explanations
5. **Inductive Learning** - Handles new artists/events without retraining

## 📞 Support

For issues or questions about the implementation, check:

- Configuration in `config.py`
- Cultural taxonomy in `data/cultural_constants.py`
- Model architecture in `models/gnn_model.py`

---

**Ready to start? Run:** `./run_demo.sh`
