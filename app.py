"""Entry point for Hugging Face Spaces"""
import sys
import os
"""Entry point for Hugging Face Spaces"""
from app_hf import *

from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import everything from your main app
from src.frontend.app import *
