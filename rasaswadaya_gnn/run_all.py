#!/usr/bin/env python3
"""
Master Execution Script
Runs all pipeline steps sequentially:
1. Generate dataset
2. Integrate real artists
3. Export to CSV
4. Run training pipeline
"""

import subprocess
import sys
import os
from datetime import datetime

def print_header(message):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {message}")
    print("="*70 + "\n")

def run_step(step_num, description, script_name):
    """Run a single pipeline step"""
    print_header(f"STEP {step_num}: {description}")
    
    start_time = datetime.now()
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout per step
        )
        
        if result.returncode == 0:
            print(result.stdout)
            elapsed = (datetime.now() - start_time).total_seconds()
            print(f"\n✅ {description} completed successfully ({elapsed:.1f}s)")
            return True
        else:
            print(f"❌ Error in {description}:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⚠️  {description} timed out (>5 minutes)")
        return False
    except Exception as e:
        print(f"❌ Exception in {description}: {e}")
        return False

def check_requirements():
    """Check if required packages are installed"""
    print_header("Checking Requirements")
    
    required_packages = ['numpy', 'pandas']
    missing = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} not found")
            missing.append(package)
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
        print("Run: pip install " + " ".join(missing))
        response = input("\nInstall missing packages now? (y/n): ")
        
        if response.lower() == 'y':
            print("\nInstalling packages...")
            subprocess.run([sys.executable, "-m", "pip", "install"] + missing)
            return True
        else:
            print("\nPlease install missing packages before continuing.")
            return False
    
    print("\n✅ All required packages installed")
    return True

def verify_outputs():
    """Verify all expected output files were created"""
    print_header("Verifying Outputs")
    
    expected_files = [
        "data/sample_dataset/rasaswadaya_dataset_updated.json",
        "data/sample_dataset/rasaswadaya_dataset_updated.pkl",
        "data/sample_dataset/rasaswadaya_dataset_with_real_artists.json",
        "data/sample_dataset/csv_export_updated/users.csv",
        "data/sample_dataset/csv_export_updated/artists.csv",
        "data/sample_dataset/csv_export_updated/events.csv",
        "data/sample_dataset/csv_export_updated/follows.csv",
        "data/sample_dataset/csv_export_updated/attends.csv",
    ]
    
    all_exist = True
    for filepath in expected_files:
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"✅ {filepath} ({size:,} bytes)")
        else:
            print(f"❌ {filepath} - NOT FOUND")
            all_exist = False
    
    return all_exist

def main():
    """Main execution function"""
    print_header("Rasaswadaya GNN - Complete Pipeline Execution")
    print("This will run all 4 steps:")
    print("  1. Generate dataset (200 users, 100 artists, 150 events)")
    print("  2. Integrate 15 real Sri Lankan artists")
    print("  3. Export to CSV format")
    print("  4. Run training pipeline setup")
    print()
    
    start_total = datetime.now()
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Define pipeline steps
    steps = [
        (1, "Generate Dataset", "generate_new_data.py"),
        (2, "Integrate Real Artists", "integrate_real_artists.py"),
        (3, "Export to CSV", "export_to_csv.py"),
        (4, "Run Training Pipeline", "train_model.py"),
    ]
    
    # Run all steps
    results = []
    for step_num, description, script in steps:
        success = run_step(step_num, description, script)
        results.append((step_num, description, success))
        
        if not success:
            print(f"\n⚠️  Step {step_num} failed. Continue with remaining steps? (y/n): ")
            response = input()
            if response.lower() != 'y':
                break
    
    # Summary
    print_header("Execution Summary")
    
    for step_num, description, success in results:
        status = "✅ SUCCESS" if success else "❌ FAILED"
        print(f"Step {step_num}: {description:.<50} {status}")
    
    # Verify outputs
    if all(success for _, _, success in results):
        print()
        verify_outputs()
    
    # Total time
    total_time = (datetime.now() - start_total).total_seconds()
    print(f"\n⏱️  Total execution time: {total_time:.1f} seconds")
    
    # Next steps
    if all(success for _, _, success in results):
        print_header("✅ ALL STEPS COMPLETED SUCCESSFULLY!")
        print("Next steps:")
        print("  1. View CSV files: ls -lh data/sample_dataset/csv_export_updated/")
        print("  2. Explore data: python3")
        print("     >>> import pandas as pd")
        print("     >>> df = pd.read_csv('data/sample_dataset/csv_export_updated/artists.csv')")
        print("     >>> print(df.head())")
        print("  3. Run full demo: python3 demo.py")
        print()
    else:
        print_header("⚠️  Some Steps Failed")
        print("Check error messages above for details.")
        print("You may need to:")
        print("  - Install missing packages: pip install numpy pandas")
        print("  - Check file permissions")
        print("  - Verify Python version: python3 --version")
        print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Execution interrupted by user")
        sys.exit(1)
