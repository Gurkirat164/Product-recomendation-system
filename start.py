#!/usr/bin/env python3
import os
import sys

# Simple startup script for Pterodactyl with minimal dependencies
print("Product Recommendation System - Simple Startup")
print("=" * 45)

# Check Python version
print(f"Python version: {sys.version}")

# Get port from environment
port = os.environ.get('SERVER_PORT', '25565')
print(f"Port: {port}")

# Check for data files
data_files = ["train_data.csv", "trending_items.csv"]
for file in data_files:
    if os.path.exists(file):
        print(f"✓ Found {file}")
    else:
        print(f"⚠ Missing {file}")

print("\nStarting Flask application...")

try:
    # Set port environment variable
    os.environ['PORT'] = str(port)
    
    # Import and run the Flask app
    from app import app
    app.run(host='0.0.0.0', port=int(port), debug=False)
    
except ImportError as e:
    print(f"Import error: {e}")
    print("Please install required dependencies:")
    print("pip install flask pandas scikit-learn numpy")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
