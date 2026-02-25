#!/bin/bash

echo "=================================================="
echo "  Rasaswadaya.lk GNN Model - Quick Start"
echo "=================================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 Running demo..."
echo ""

python demo.py

echo ""
echo "=================================================="
echo "  Demo complete!"
echo "=================================================="
