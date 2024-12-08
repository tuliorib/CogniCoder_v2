# src/core/utils/config_handler.py

import os
import yaml
from typing import Dict, Any, Optional

def load_config(config_name: str) -> Optional[Dict[str, Any]]:
    # Get the project root directory
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    
    # Construct the path to the config file
    config_path = os.path.join(project_root, 'config', config_name)

    try:
        with open(config_path, 'r') as config_file:
            return yaml.safe_load(config_file)
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        print("Please ensure the config file exists and the path is correct.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing the configuration file: {e}")
        return None

# Usage
# config = load_config('document_store.config')
